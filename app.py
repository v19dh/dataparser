from urllib import response
from flask import Flask, jsonify, request, make_response
from flask_restful import Resource, Api, reqparse, abort


app = Flask(__name__)

api = Api(app)

beacons = [
        {
		  "Beacon_Id": 0, 
		  "DateTime": "2022",
		  "TemperatureData":
		      {
                "Temperature":35
		      },
		  "BatteryData":
		      {
               "Voltage":12
		       }
		},
		{
		  "Beacon_Id": 1, 
		  "DateTime": "2022",
		  "TemperatureData":
		      {
                "Temperature":22
		      },
		  "BatteryData":
		      {
               "Voltage":22
		       }
		},
		{
		  "Beacon_Id": 2, 
		  "DateTime": "2022",
		  "TemperatureData":
		      {
                "Temperature":33
		      },
		  "BatteryData":
		      {
               "Voltage":33	
		       }
		}
]

beacon_post_args = reqparse.RequestParser()
beacon_post_args.add_argument("Beacon_Id",type=str,required=True)	
beacon_post_args.add_argument("DateTime",type=str,required=True)	
beacon_post_args.add_argument("TemperatureData",type=str,required=True)	
beacon_post_args.add_argument("BatteryData",type=str,required=True)	

class BeaconsList(Resource):
	def get(self):
		return beacons

class Home(Resource):

	def get(self):

		return beacons

	
	def post(self):

		if request.is_json:
			req = request.get_json()
		response = {
			"message":"JSON RECIEVED",
		}	
		res = make_response(jsonify(response),200)
		# print(req)
		# print(type(req))
		for i in req:
			print({"Beacon_Id:":i["Beacon_Id"],"DateTime":i["DateTime"],"TemperatureData":i["TemperatureData"]},{"Beacon_Id:":i["Beacon_Id"],"DateTime":i["DateTime"],"BatteryData":i["BatteryData"]})
           
        		
		
		
			
	
			  
# adding the defined resources along with their corresponding urls
api.add_resource(Home, '/')
api.add_resource(BeaconsList, '/beaconslist')



# driver function
if __name__ == '__main__':

	app.run(debug = True)

