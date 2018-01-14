from flask import Flask, jsonify, request
from pymongo import MongoClient
import QnA
import message


app = Flask(__name__)
client = MongoClient()

db = client["farewell"]
collection, collection_clear = db.bye, db.clear

@app.route('/keyboard')
def keyboard():
    dataSend = {
        "type": "buttons",
        "buttons": ["똑똑"]
    }
    return jsonify(dataSend)


@app.route('/message', methods=['POST'])
def Message():
    dataReceive = request.get_json()
    user_key = dataReceive['user_key']  # user id get
    content = dataReceive['content']    # user message get

    #First Phase
    try:
        phase = getStatus(user_key, collection)["phase"]
    except:
        phase = 1

    if phase == 1:
        


    return jsonify(dataSend)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000, debug=True)