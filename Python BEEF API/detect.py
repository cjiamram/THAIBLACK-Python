from flask import Flask
from flask import request
from datetime import datetime
#from tensorflow.keras.models import load_model
from flask_cors import CORS,cross_origin
#from garmentPredict import GarmentPredict
from beefPredict import BeefPredict 
import json
from flask import jsonify

app = Flask(__name__)

cors = CORS(app, resources={r"/service": {"origins": "*","Access-Control-Allow-Methods":"POST"}})
@app.route("/hello")
def hello():
    return "<h1 style='color:blue'>Hello Machine Learning Site Project!</h1>"

#*****************************************************************
#@app.route("/service",  methods = ['POST'])
#@cross_origin(origin='*',headers=['access-control-allow-origin','Content-Type;application/json;charset=UTF-8','Access-Control-Allow-Methods: POST'])
#def jsonProcess():
#    data=request.get_json()
#    image=data['image']
#    GP = GarmentPredict()
#    result=GP.prediction(image)
#    return result
#*****************************************************************
@app.route('/createDir/<folder>', methods=['GET'])
def createDir(folder):
    BP=BeefPredict()
    msg=BP.createFolder(folder)
    return msg

@app.route('/classifyBeefElement/<folder>', methods=['GET'])
@cross_origin(origin='*',headers=['access-control-allow-origin','Content-Type;application/json;charset=UTF-8','Access-Control-Allow-Methods: POST'])
def classifyBeefElement(folder):
    BP=BeefPredict()
    jsonObj=BP.classifyBeefElement(folder)
    return jsonObj


@app.route('/classifyBeefElementOne/<folder>/<file>', methods=['GET'])
@cross_origin(origin='*',headers=['access-control-allow-origin','Content-Type;application/json;charset=UTF-8','Access-Control-Allow-Methods: POST'])
def classifyBeefElementOne(folder,file):
    BP=BeefPredict()
    jsonObj=BP.classifyByElementOne(folder,file)
    return jsonObj


@app.route('/getImgFromFolder/<folder>', methods=['GET'])
@cross_origin(origin='*',headers=['access-control-allow-origin','Content-Type;application/json;charset=UTF-8','Access-Control-Allow-Methods: GET'])
def getImgFromFolder(folder):
    BP=BeefPredict()
    jsonObj=BP.getImgFromFolder(folder)
    return jsonObj



@app.route('/fileClassify/<folder>', methods=['GET'])
@cross_origin(origin='*',headers=['access-control-allow-origin','Content-Type;application/json;charset=UTF-8','Access-Control-Allow-Methods: GET'])
def fileClassify(folder):
    BP=BeefPredict()
    return  BP.classifyByFile(folder)

@app.route('/classify/', methods=['GET','POST'])
@cross_origin(origin='*',headers=['access-control-allow-origin','Content-Type;application/json;charset=UTF-8','Access-Control-Allow-Methods: POST'])
def classify():
    data=request.get_json()
    folder=data['folder']
    dl=data['dl']
    w=data['w']
    h=data['h']
    BP=BeefPredict()
    return  BP.classifyElement(folder,dl,w,h)

#@app.route('/getElementFile', methods=['POST'])
#@cross_origin(origin='*',headers=['access-control-allow-origin','Content-Type;application/json;charset=UTF-8','Access-Control-Allow-Methods: POST'])
#def getElementFile():
#    data=request.get_json()
#    file=data["file"] 
#    BP=BeefPredict()
#    jsonObj= BP.getElementFile(file)
#    return jsonObj


@app.route('/getElementDetail', methods=['GET','POST'])
@cross_origin(origin='*',headers=['access-control-allow-origin','Content-Type;application/json;charset=UTF-8','Access-Control-Allow-Methods: POST'])
def getElementDetail():
    data=request.get_json()
    file=data["file"] 

    x1=data["area"]['x1']
    y1=data["area"]['y1']
    x2=data["area"]['x2']
    y2=data["area"]['y2']
    W=data["area"]['W']
    H=data["area"]['H']
    area={"x1":x1,"y1":y1,"x2":x2,"y2":y2}
    BP=BeefPredict()
    jsonObj= BP.getElementDetail(file,area,W,H)
    return jsonObj



@app.route('/cropClassify', methods=['GET','POST'])
@cross_origin(origin='*',headers=['access-control-allow-origin','Content-Type;application/json;charset=UTF-8','Access-Control-Allow-Methods: POST'])
def cropClassify():
    data=request.get_json()
    file=data['file'] 
    x1=data["area"]['x1']
    y1=data["area"]['y1']
    x2=data["area"]['x2']
    y2=data["area"]['y2']
    W=data["area"]['W']
    H=data["area"]['H']
    area={"x1":x1,"y1":y1,"x2":x2,"y2":y2}
    BP=BeefPredict()
    jsonObj=BP.classifyAfterCrop(file,area,W,H)
    return jsonObj

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0')