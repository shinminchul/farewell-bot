from flask import Flask, jsonify, request
from pymongo import MongoClient
import message


app = Flask(__name__)
client = MongoClient()

db = client["farewell"]
collection, collection_clear = db.test, db.clear