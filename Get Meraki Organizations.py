import requests
import json
import pandas as pd
url = "https://dashboard.meraki.com/api/v0/organizations"
payload={}
headers = {
  'X-Cisco-Meraki-API-Key': '207e4c449628b29182e750cfded9370022aacf6c',
  'Content-Type': 'application/json'
}
response = requests.get(url=url, headers=headers, data=payload).json()
print(response)
jsonfile = open("Organization.json","w")
jsonfile.write (json.dumps(response))
jsonfile.close()
df_json = pd.read_json("Organization.json")
df_json.to_excel("Organization.xlsx")