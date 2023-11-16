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


