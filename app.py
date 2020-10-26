from flask import Flask, jsonify , request
from flask_restful import Api,Resource

app  = Flask(__name__)
api = Api(app)

def validatePost(data, function):
  if(function == "add"):
      if "x" not in data or "y" not in data:
          return 301
      else:
          return 200

class Add(Resource):
    def post(self):
        data = request.get_json()
        status_code = validatePost(data, "add")
        if (status_code != 200):
            retJson = {
                "Message" : "Operator Error",
                "status" : status_code
            }
            return jsonify(retJson)
        else:
            x = data["x"]
            y = data["y"]
            x = int(x)
            y = int(y)
            ret = x + y
            retMap = {
                "Message" : ret,
                "status" : 200
            }
            return jsonify(retMap)

class Subtract(Resource):
    def post(self):
        data = request.get_json()
        x = data["x"]
        y = data["y"]
        x = int(x)
        y = int(y)
        ret = x - y
        retMap = {
            "Message" : ret,
            "status" : 200
        }
        return jsonify(retMap)

class Multiply(Resource):
    def post(self):
        data = request.get_json()
        x = data["x"]
        y = data["y"]
        x = int(x)
        y = int(y)
        ret = x * y
        retMap = {
            "Message" : ret,
            "status" : 200
        }
        return jsonify(retMap)

class Divide(Resource):
    def post(self):
        data = request.get_json()
        x = data["x"]
        y = data["y"]
        x = int(x)
        y = int(y)
        ret = x / y
        retMap = {
            "Message" : ret,
            "status" : 200
        }
        return jsonify(retMap)


@app.route('/')
def hola():
    return "Hello from my second app!"

api.add_resource(Add, "/add")
api.add_resource(Subtract, "/subtract")
api.add_resource(Multiply, "/multiply")
api.add_resource(Divide, "/divide")

if(__name__)=="__main__":
    app.run(debug=True)
