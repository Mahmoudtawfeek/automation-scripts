import requests

url = "https://api.meraki.com/api/v1/organizations"

payload = None

headers = {
    "Content-Type": "application/json",
    "Accept": "application/json",
    "X-Cisco-Meraki-API-Key": "207e4c449628b29182e750cfded9370022aacf6c"
}

response = requests.request('GET', url, headers=headers, data = payload)

print(response.text.encode('utf8'))

