import requests
import json
import jsonpath
import pytest

file = open("C:\\Users\\ovonel\\PycharmProjects\\pythonProject8\\utilities\\request.json", "r")
apiURL = "http://thetestingworldapi.com/api/studentsDetails"

#Loading file into the JSON
json_payload=json.loads(file.read())

        #Making request
response=requests.post(apiURL, json_payload)
print(response.text)

print(file.read())

