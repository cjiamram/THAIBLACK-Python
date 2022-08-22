from tensorflow.keras.models import load_model
from imutils import paths
from PIL import Image
from collections import OrderedDict
import argparse
import numpy as np
import tensorflow
import imutils
import cv2
import json
import base64
import os
from flask import jsonify


class BeefPredict:
	
	#def __init__(self):


	def image_to_feature_vector(self,image, size=(32, 32)):
		return cv2.resize(image, size).flatten()
	
	def getModelFile(self):
		f = open('beefClass.json',)
		data = json.load(f)
		return data["modelFile"]

		
	def getImgPath(self):
		f = open('beefClass.json',)
		data = json.load(f)
		return data["imgPath"]

	def getRoot(self):
		f = open('beefClass.json',)
		data = json.load(f)
		return data["root"]

	def getClassVAR(self,key):
		f = open('beefClass.json',)
		data = json.load(f)
		return data[key]



	def getBeefClass(self,key,index):
		f = open('beefClass.json',)
		data = json.load(f)
		return data["CLASSES"][index]

	
	def getBeefElement(self,key):
		f = open('beefClass.json',)
		data = json.load(f)
		return data["ELements"]
	
	def interpolate(self,x,picSize,realSize):
		return realSize*x/picSize

	
		
	def get_imageArray(self,image):
		width, height = image.size
		pixel_values = list(image.getdata())
		if image.mode == "RGB":
			channels = 3
		elif image.mode == "L":
			channels = 1
		else:
			print("Unknown mode: %s" % image.mode)
			return None
	
		pixel_values = np.array(pixel_values).reshape((width, height, channels))
		return pixel_values

	def getAvgBeefColor(beefDics):
		sum=0
		n=0
		for a in beefDics:
			if a["ElementType"]==1:
				sum=sum+a["BeefColor"]
				n=n+1
		return sum/n 



	def getBeefGrade(self,model,fileName,beefClass):
		image = cv2.imread(fileName)
		features = self.image_to_feature_vector(image) / 255.0
		features = np.array([features])
		probs = model.predict(features)[0]
		prediction = probs.argmax(axis=0)
		beefGrades={}
		if(probs[prediction] * 100>70):
			beefGrades ={"class":beefClass[prediction]['class'],"weight":beefClass[prediction]['weight'],"confidence":probs[prediction] * 100} 
		return beefGrades

	
	def getBeefInfo(self,beefDics):
		sumBeef=0
		sumFat=0
		sum=0
		n=0
		for a in beefDics:
			if a["ElementType"]==0:
				sumBeef=sumBeef+1
				sum=sum+a["BeefColor"]
				n=n+1
			else:
				if a["ElementType"]==1:
					sumFat=sumFat+1
		beefElements={"beef":sumBeef*3600,"fat":sumFat*3600,"ratio":(sumFat/sumBeef)*100,"beefColor":sum/n}
		return beefElements
	
	def isValidFat(self,im,d):
		w, h = im.size
		A1=(0,0,d,d)
		A2=(w-d,0,w,h+d)
		A3=(0,h-d,w+d,h+d)
		A4=(w-d,h-d,w,h)
		image1=im.crop(A1)
		image2=im.crop(A2)
		image3=im.crop(A3)
		image4=im.crop(A4)
		avg1=np.average(self.get_imageArray(image1))
		avg2=np.average(self.get_imageArray(image2))
		avg3=np.average(self.get_imageArray(image3))
		avg4=np.average(self.get_imageArray(image4))
		
		b1=(avg1>=60)&(avg1<160)
		b2=(avg2>=60)&(avg2<160)
		b3=(avg3>=60)&(avg3<160)
		b4=(avg4>=60)&(avg4<160)

		f1=(avg1>=160)&(avg1<250)
		f2=(avg2>=160)&(avg2<250)
		f3=(avg3>=160)&(avg3<250)
		f4=(avg4>=160)&(avg4<250)

		flag=True
		if(b1|b2|b3|b4)&(f1|f2|f3|f4):
			flag=True
		else:
			flag=False

	
		return flag
	
	
	def getClassifyBeefElement(self,fileName):
		model = load_model(self.getModelFile())
		beefElementsClass = self.getClassVAR("ELements")
		beefClass=self.getClassVAR("CLASSES")
		im = Image.open(fileName, 'r')
		width, height = im.size
		dx=60
		dy=60
		sx=0
		sy=0
		beefDics=[]
		while(sy<=height-dy):
			sx=0
			while(sx<=width-dx):
				area=(sx, sy, sx+dx, sy+dy)
				sx=sx+dx
				image = im.crop(area)
				avg=np.average(self.get_imageArray(image))
				elmType=0
				if((avg>=60)&(avg<160)):
					elmType=0
				else:
					if((avg>=160)&(avg<250)):
						elmType=1
						flag=self.isValidFat(im,20)
						if (avg>240)&(flag==False):
							elmType=2
					else:
						elmType=2
						

				label = beefElementsClass[elmType]["elementName"]
				beefDic={"Label": label,"ElementType":elmType,"BeefColor":avg}

				beefDics.append(beefDic)
			sy=sy+dy
		beefGrades=self.getBeefGrade(model,fileName,beefClass)
		elementInfo=self.getBeefInfo(beefDics)
		parentPath=self.getClassVAR("parentPath")
		linkPath=self.getClassVAR("root")
		fName=fileName.replace(parentPath,linkPath)
		print(fName)
		beefInfo={"fileName":fName,"beefInfo":elementInfo,"beefGrades":beefGrades}
		return  beefInfo

	
	def classifyByElementOne(self,folder,file):
		imagePath=self.getImgPath()+folder+"/"+file
		print(imagePath)
		beefInfo=self.getClassifyBeefElement(imagePath)
		return jsonify(beefInfo)
	
	def classifyBeefElement(self,folder):
		parent=self.getImgPath()
		path = os.path.join(parent, folder)
		beefInfos=[]
		for imagePath in paths.list_images(path):
			beefInfo=self.getClassifyBeefElement(imagePath)
			beefInfos.append(beefInfo)
		return jsonify(beefInfos)


	

	
	def classifyByFile(self,folder):
		CLASSES=self.getClassVAR("CLASSES")
		model = load_model(self.getModelFile())
		parent=self.getRoot()
		path = os.path.join(parent, folder)
		labels=[]
		for imagePath in paths.list_images(path):
			image = cv2.imread(imagePath)
			features = self.image_to_feature_vector(image) / 255.0
			features = np.array([features])
			probs = model.predict(features)[0]
			prediction = probs.argmax(axis=0)
			if(probs[prediction] * 100>70):
				label ={"fileName":imagePath,"class":CLASSES[prediction]['class'],"weight":CLASSES[prediction]['weight'],"confidence":probs[prediction] * 100} 
				labels.append(label)
		return json.dumps(labels)

	def classifyElement(self,folder,dl,w,h):
		CLASSES=self.getClassVAR("CLASSES")
		model = load_model(self.getModelFile())
		parent=self.getRoot()
		path = os.path.join(parent, folder)
		dx=dl
		dy=dl
		labels=[]
		for imagePath in paths.list_images(path):
			im = Image.open(imagePath, 'r')
			sx=0
			sy=0
			(width, height) = im.size
			for i in range(0,width-w,dx):
				for j in range(0,height-h,dy):
					area = (i, j, i+w, j+h)
					image = im.crop(area)
					img=np.array(image)
					features = self.image_to_feature_vector(img) / 255.0
					features = np.array([features])
					probs = model.predict(features)[0]
					prediction = probs.argmax(axis=0)
					if(probs[prediction] * 100>70):
						label ={"fileName":imagePath,"area":area,"class":CLASSES[prediction]['class'],"weight":CLASSES[prediction]['weight'],"confidence":probs[prediction]*100} 
						labels.append(label)
		return json.dumps(labels)

	
	


	def getElementDetail(self,file,area,W,H):
		parent=self.getImgPath()
		path = parent+file
		im = Image.open(path, 'r')
		(picW, picH) = im.size
		x1=self.interpolate(area["x1"],picW,W)
		y1=self.interpolate(area["y1"],picH,H)
		x2=self.interpolate(area["x2"],picW,W)
		y2=self.interpolate(area["y2"],picH,H)
		area=(x1,y1,x2,y2)
		image = im.crop(area)
		width, height = im.size
		TH=height
		TW=width
		dx=50
		dy=50
		sx=0
		#sy=0
		sx1=x1
		sy1=y1
		accBeef=0
		accFat=0
		while(TH>0):
			sx=0
			TW=width
			while(TW>0):
				sx+=dx
				area1=(sx1, sy1, sx1+dx, sy1+dy)
				TW-=dx
				sx1+=dx
				image = im.crop(area1)
				avg=np.average(self.get_imageArray(image))
				if((avg>=60)&(avg<160)):
					accBeef+=1
				else:
					if((avg>=160)&(avg<250)):
						accFat+=1
			sy1+=dy
			TH-=dy
		beefDic={"fat":accFat,"fatArea":accFat*250,"accBeef":accBeef,"beefArea":accBeef*250,"ratio":(accFat/accBeef)*100}	
		return json.dumps(beefDic)
               
	def classifyAfterCrop(self,file,area,W,H):
		model = load_model(self.getModelFile())
		CLASSES=self.getClassVAR("CLASSES")
		parent=self.getRoot()
		path = parent+"/"+file
		im = Image.open(path, 'r')
		(picW, picH) = im.size
		#print(area)
		x1=self.interpolate(area["x1"],picW,W)
		y1=self.interpolate(area["y1"],picH,H)
		x2=self.interpolate(area["x2"],picW,W)
		y2=self.interpolate(area["y2"],picH,H)
		area=(x1,y1,x2,y2)
		image = im.crop(area)
		img=np.array(image)
		features = self.image_to_feature_vector(img) / 255.0
		features = np.array([features])
		probs = model.predict(features)[0]
		prediction = probs.argmax(axis=0)
		label ={"fileName":path,"area":area,"class":CLASSES[prediction]['class'],"weight":CLASSES[prediction]['weight'],"confidence":probs[prediction] * 100}
		return json.dumps(label)


	def getImgFromFolder(self,folder):
		parent=self.getImgPath()
		path = os.path.join(parent, folder)
		beefInfos=[]
		for imagePath in paths.list_images(path):
			imgName={"imgName":imagePath}
			beefInfos.append(imgName)
		return jsonify(beefInfos)


	def createFolder(self,folder):
		try:
			parent=self.getImgPath()
			path = os.path.join(parent, folder)
			os.mkdir(path)
			return json.dumps({"flag":True}) 
		except:
 			return json.dumps({"flag":False,"message":"Error"})



	
		