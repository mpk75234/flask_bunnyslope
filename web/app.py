'''
Requirements:
User registration
Each user is allocated 10 tokens.
User can store a sentence for 1 token.
User can retrieve sentence from mongodb for 1 token
'''
from flask import Flask, jsonify, request
from flask_restful import Api, Resource
from pymongo import MongoClient
import bcrypt

app = Flask(__name__)
api = Api(app)

client = MongoClient("mongodb://db:27017")
db = client.newDB
users = db["users"]

class Register(Resource):
    def post(self):
        #get POST data
        data = request.get_json()
        #validate username, password
        username = data["username"]
        password = data["password"]

        hashed_pw = bcrypt.hashpw(password.encode(encoding="utf-8"), bcrypt.gensalt(10))
        #store username/password to mongodb
        users.insert_one({
            "username" : username,
            "password" : hashed_pw,
            "sentence" : "",
            "tokens" : 10
        })

        retJson = {
            "status" : 200,
            "msg" : "User API signup completed succesfully. Welcom to the API"
        }
        return jsonify(retJson)

def verifyPw(username, password):
    hashed_pw = users.find({
    "username":username
    })[0]["password"]

    if bcrypt.hashpw(password.encode('utf-8'), hashed_pw) == hashed_pw:
        return True
    else:
        return False
def tokenCount(username):
    tokens = users.find({
    "username":username
    })[0]["tokens"]
class Store(Resource):
    def post(self):
        data = request.get_json()
        username = data["username"]
        password = data["password"]
        sentence = data["sentence"]
        tokens = data["tokens"]

        #validaet username/Password
        correct_pw = verifyPw(username, password)
        if not correct_pw:
            retJson = {
            "status" : 403,
            "message" : "ACCESS DENIED  check your password"
            }
            return jsonify(retJson)
        tokens = tokenCount(username)
        if tokens <= 0:
            retJson = {
            "status" : 302,
            "message" : "you do not have enough tokens for this opeation:",
            "tokens" : tokens
            }
            return jsonify(retJson)
        users.update({
            "username": username
        }, {
            "$set":{"sentence":sentence,
                    "toekns":tokens-1}
        })
        retJson = {
        "status":200,
        "message": "sentence saved successfully"
        }
        return jsonify(retJson)


api.add_resource(Register, '/register')
api.add_resource(Store, '/store')

if(__name__)=="__main__":
    app.run(host='0.0.0.0')
