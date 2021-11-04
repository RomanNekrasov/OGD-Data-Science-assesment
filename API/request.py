
import requests
import json

url = 'http://0.0.0.0:5000/api/'

#data = [[3, 0, 22, 1, 0, 7.25, 0, 0, 1, 3, 1]] # dead
data = [[1,	1,	47.000000,	1,	1,	52.5542,	0,	0,	0,	2,	0]] #survived
j_data = json.dumps(data)
headers = {'content-type': 'application/json', 'Accept-Charset': 'UTF-8'}
r = requests.post(url, data=j_data, headers=headers)
print(r, r.text)