#from flask import jsonify
import json
f = open('config.json',)
data = json.load(f)
print(data["fileConfig"]["urlUpload"])
    