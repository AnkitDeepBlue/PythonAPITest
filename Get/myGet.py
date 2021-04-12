import requests
import json
import jsonpath

# URL
url = "https://reqres.in/api/users?page=2"

response=requests.get(url)

json_respose= json.loads(response.text)

mylist=[]



for i in range (0,6):
    first_name= jsonpath.jsonpath(json_respose, 'data['+str(i)+'].first_name')

    mylist.append(first_name[0])


print(mylist)
assert "Michael" and "Howell" and "Tobias" in mylist

print("Git attached")


#Header part

# print(response.status_code)
# print(response.headers)
# print(response.headers.get('Content-Type'))
# print(response.cookies)
# print(response.elapsed)
# assert 200 == response.status_code

#Respose Part

