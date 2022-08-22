from flask import Flask
from flask import request
from datetime import datetime
from keras.models import load_model
from flask_cors import CORS,cross_origin

import numpy as np
import tensorflow
import imutils
import cv2
import json
import base64
import os

app = Flask(__name__)

cors = CORS(app, resources={r"/service": {"origins": "*","Access-Control-Allow-Methods":"POST"}})
#app.config['CORS_HEADERS'] = 'Content-Type;application/json;charset=utf-8'
#app.config['CORS_HEADERS'] = 'Access-Control-Allow-Methods: POST'





CLASSES = ["A","AA","B","BB","C","CC","DD","E","EE","KK","N"]
CLASSES_A=["A01","A02","A03","A04"]
CLASSES_AA=["AA02"]
CLASSES_B=['B01', 'B04', 'B06', 'B03', 'B07', 'B02', 'B05']
CLASSES_BB= ["BB04","BB05"]
CLASSES_C=["C01","C02","C03","C04"]
CLASSES_CC=["CC02","CC03","CC05"] 
CLASSES_DD=['DD02', 'DD03','DD04', 'DD05']
CLASSES_E=['E01', 'E02','E03', 'E04']
CLASSES_EE=['EE01', 'EE03','EE04', 'EE05','EE06','EE07','EE08','EE09']  
CLASSES_KK=['KK01','KK02','KK03','KK04','KK05']
CLASSES_N= ['N01','N04'] 


def image_to_feature_vector(image, size=(32, 32)):
	return cv2.resize(image, size).flatten()



def saveFile(data):
    now = str(datetime.now())
    now = str(now.replace(".", "")) 
    now = str(now.replace(":",""))
    now = str(now.replace(" ",""))
    fnow = "imgTemp/"+now+".jpg" 
    with open(fnow, 'wb') as f:
        f.write(base64.decodebytes(data.split(',')[1].encode()))
    return fnow

@app.route("/hello")
def hello():
    return "<h1 style='color:blue'>Hello There!</h1>"

@app.route("/service",  methods = ['POST'])
@cross_origin(origin='*',headers=['access-control-allow-origin','Content-Type;application/json;charset=UTF-8','Access-Control-Allow-Methods: POST'])
def jsonProcess():


    modelFile="output/model_R9.hdf5"
    #modelFileKK= "output/KKModel/model_KK.hdf5"
    #modelFileN= "output/NModel/model_N.hdf5"

    model = load_model(modelFile)

    data=request.get_json()
    image=data['image']
    path=saveFile(image)

    image = cv2.imread(path)
    os.remove(path)
    features = image_to_feature_vector(image)/255.0
    features = np.array([features])

    probs = model.predict(features)[0]
    prediction = probs.argmax(axis=0) 
    
    labelProb=""
    labelClass=""

    if(probs[prediction] * 100>70):

        labelProb="{:.2f}%".format(probs[prediction] * 100)
        labelClass=CLASSES[prediction]

        if(CLASSES[prediction]=="A"):
            modelFileA= "output/AModel/model_A_1.hdf5"
            modelA= load_model(modelFileA)
            probA=modelA.predict(features)[0]
            predicA=probA.argmax(axis=0)
            labelProb="{:.2f}%".format(probA[predicA] *100)
            labelClass=CLASSES_A[predicA]

        elif CLASSES[prediction]=="B":
            modelFileB= "output/BModel/model_B.hdf5"
            modelB= load_model(modelFileB)
            probB=modelB.predict(features)[0]
            predicB=probB.argmax(axis=0)
            labelProb="{:.2f}%".format(probB[predicB] * 100)
            labelClass=CLASSES_B[predicB]

        elif CLASSES[prediction]=="BB":
            modelFileBB= "output/BBModel/model_BB.hdf5"
            modelBB= load_model(modelFileBB)
            probBB=modelBB.predict(features)[0]
            predicBB=probBB.argmax(axis=0)
            labelProb="{:.2f}%".format(probBB[predicBB] * 100)
            labelClass=CLASSES_BB[predicBB]

        elif CLASSES[prediction]=="C":
            modelFileC= "output/CModel/model_C.hdf5"
            modelC= load_model(modelFileC)
            probC=modelC.predict(features)[0]
            predicC=probC.argmax(axis=0)
            labelProb="{:.2f}%".format(probC[predicC] * 100)
            labelClass=CLASSES_C[predicC]

        elif CLASSES[prediction]=="CC":
            modelFileCC= "output/CCModel/model_CC.hdf5"
            modelCC= load_model(modelFileCC)
            probCC=modelCC.predict(features)[0]
            predicCC=probCC.argmax(axis=0)
            labelProb="{:.2f}%".format(probCC[predicCC] * 100)
            labelClass=CLASSES_CC[predicCC]
       
       
        elif CLASSES[prediction]=="DD":
            modelFileDD= "output/DDModel/model_DD.hdf5"
            modelDD= load_model(modelFileDD)
            probDD=modelDD.predict(features)[0]
            predicDD=probDD.argmax(axis=0)
            labelProb="{:.2f}%".format(probDD[predicDD] * 100)
            labelClass=CLASSES_DD[predicDD]


        elif CLASSES[prediction]=="E":
            modelFileE= "output/EModel/model_E.hdf5"
            modelE= load_model(modelFileE)
            probE=modelE.predict(features)[0]
            predicE=probE.argmax(axis=0)
            labelProb="{:.2f}%".format(probE[predicE] * 100)
            labelClass=CLASSES_E[predicE]

            
        elif CLASSES[prediction]=="EE":
            modelFileEE= "output/EEModel/model_EE.hdf5"
            modelEE= load_model(modelFileEE)
            probEE=modelEE.predict(features)[0]
            predicEE=probEE.argmax(axis=0)
            labelProb="{:.2f}%".format(probEE[predicEE] * 100)
            labelClass=CLASSES_EE[predicEE]


        elif CLASSES[prediction]=="KK":
            modelFileKK= "output/KKModel/model_KK.hdf5"
            modelKK= load_model(modelFileKK)
            probKK=modelKK.predict(features)[0]
            predicKK=probKK.argmax(axis=0)
            labelProb="{:.2f}%".format(probKK[predicKK] * 100)
            labelClass=CLASSES_KK[predicKK]

        elif CLASSES[prediction]=="N":
            modelFileN= "output/NModel/model_N.hdf5"
            modelN= load_model(modelFileN)
            probN=modelN.predict(features)[0]
            predicN=probN.argmax(axis=0)
            labelProb="{:.2f}%".format(probN[predicN] * 100)
            labelClass=CLASSES_N[predicN]
    

    
    return json.dumps({'prediction':labelProb,'class':labelClass})


if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0')