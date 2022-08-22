from keras.models import load_model
from datetime import datetime
from imutils import paths
import numpy as np
import tensorflow
import imutils
import cv2
import json
import base64
import os
class GarmentPredict:

	def getClassVAR(self,key):
		f = open('garmentClass.json',)
		data = json.load(f)
		return data[key]

	def saveFile(self,data):
		now = str(datetime.now())
		now = str(now.replace(".", "")) 
		now = str(now.replace(":",""))
		now = str(now.replace(" ",""))
		fnow = "imgTemp/"+now+".jpg" 
		with open(fnow, 'wb') as f:
			f.write(base64.decodebytes(data.split(',')[1].encode()))
		return fnow

	def image_to_feature_vector(self,image,size=(32, 32)):
		return cv2.resize(image, size).flatten()

	def prediction(self,image):
		modelFile=self.getClassVAR("ModelFile")
		model = load_model(modelFile)
		path=self.saveFile(image)
		image = cv2.imread(path)
		os.remove(path)
		features = self.image_to_feature_vector(image)/255.0
		features = np.array([features])
		probs = model.predict(features)[0]
		prediction = probs.argmax(axis=0)
		CLASSES= self.getClassVAR("CLASSES")

		labelProb=""
		labelClass=""
		if(probs[prediction] * 100>70):
			labelProb="{:.2f}%".format(probs[prediction] * 100)
			labelClass=""
			Key=CLASSES[prediction]["Key"]
			modelFile= CLASSES[prediction]["File"]
			if(modelFile!=""):
				CLASSES_S=self.getClassVAR(Key)
				modelS= load_model(modelFile)
				probS=modelS.predict(features)[0]
				predicS=probS.argmax(axis=0)
				labelProb="{:.2f}%".format(probS[predicS] * 100)
				labelClass=CLASSES_S[predicS]
			else:
				labelProb="0.80%"
				labelClass="AA02"
			return  json.dumps({'prediction':labelProb,'class':labelClass})
		else:
			return  json.dumps({'prediction':0,'class':"Unidentified"})  
