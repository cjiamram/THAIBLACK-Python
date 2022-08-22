from flask import Flask, request, jsonify
import requests
app = Flask(__name__)

@app.route("/send")
def send():
    res = requests.post('http://localhost:5000/api/add_message/1234', json={"mytext":"lalala"})
    if res.ok:
        print(res.json())


@app.route('/add_message', methods=['POST'])
def add_message():
    data = request.get_json()
    #user=data['username']
    #print(content['mytext'])
    return jsonify(data)


@app.route('/echo', methods=['POST'])
def receive():
   return jsonify(request.get_json())

@app.route("/")
def hello():
    return "hello world"

if __name__ == '__main__':
    app.run(debug=True)