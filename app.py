from flask import Flask , request
from flask_restful import Resource , Api,reqparse
import json ,time 

app = Flask (__name__)
api = Api(app) 

parser = reqparse.RequestParser()
parser.add_argument('info')

class Hello(Resource):
	def get(self): 
		args = parser.parse_args()
		name = args['info']
		return {"time":time.time(),"received":name}

api.add_resource(Hello,'/timestamp')

if __name__ == '__main__':
	app.run(host='0.0.0.0',port=5500)
