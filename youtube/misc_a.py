import requests
import json
import jsonpath
import allure
import logging

url="http://thetestingworldapi.com/api/studentsDetails"
data={
  "id": 500,
  "first_name": "Ankit",
  "middle_name": "",
  "last_name": "Tripathi",
  "date_of_birth": "1/1/1993"
}

file=open("C:\\Users\\ovonel\\PycharmProjects\\pythonProject8\\utilities\\request.json", "r")

payload=json.loads(file.read())

respose= requests.post(url, data= payload)
print(respose.status_code)

id=jsonpath.jsonpath(respose.json(), 'id')
print("My dynamic id is ::", id[0])




# reponse=requests.post(url, data=data)
# print (reponse.status_code)


# for i in range(0, 6):
#     data=jsonpath.jsonpath(response.json(), 'data['+str(i)+'].id')
#
#     print(data)
