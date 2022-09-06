import requests,json
headers = { 'Accept' : 'application/json', 'Content-Type' : 'application/json'}
contents =[{
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
             "Voltage":33
          }
    }]


r = requests.post('http://127.0.0.1:5000/', data=json.dumps(contents), headers=headers)
print(type(r))
print(f"Status Code: {r.status_code},Response:{r.json()}")