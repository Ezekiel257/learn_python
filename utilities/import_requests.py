#this  module is a practice on import requests
#The requests module allows you to send HTTP requests using Python.


import requests

x = requests.get('https://w3schools.com/python/demopage.htm')

#print(x.text)

#request to Get Bank Flutter API
import requests

url = 'https://api.flutterwave.com/v3/banks/NG'
headers = {
    'Authorization': 'Bearer FLWSECK_TEST-SANDBOXDEMOKEY-X'
}

a = requests.get(url, headers=headers)
#print(a.text)


#Get Flutter Bank Branch API
import requests

url = 'https://api.flutterwave.com/v3/banks/280/branches'
headers = {'Authorization' :'Bearer FLWSECK_TEST-SANDBOXDEMOKEY-X'}

branch = requests.get(url, headers=headers)
print(branch.text)

#json dump
import json

x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

#print(json.dumps(x))

quantity = 3
itemno = 567
price = 49
myorder = "I want {0} pieces of item number {1} for {2:.2f} dollars."
#print(myorder.format(quantity, itemno, price))
