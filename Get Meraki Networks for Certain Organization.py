import requests
import json
import pandas as pd


url = "https://dashboard.meraki.com/api/v0/organizations/631066897785293682/networks"

payload={}
headers = {
  'X-Cisco-Meraki-API-Key': '207e4c449628b29182e750cfded9370022aacf6c',
  'Content-Type': 'application/json'
}

response = requests.get(url=url, headers=headers, data=payload).json()

print(response)

jsonfile = open("Network-631.json","w")
jsonfile.write (json.dumps(response))
jsonfile.close()
df_json = pd.read_json("Network-631.json")
df_json.to_excel("Network-631.xlsx")