import requests
import json
import jsonpath

# URL
url = "https://reqres.in/api/users?page=2"

response=requests.get(url)

json_response=json.loads(response.text)

idlist=[]

for i in range(1, 6):
    getid=jsonpath.jsonpath(json_response, 'data['+str(i)+'].id')
    idlist.append(getid[0])

print(idlist)