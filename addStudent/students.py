import requests
import json
import jsonpath
import pytest
import allure

from addStudent.apiStudents import Test_apiEndToEnd

allure.description("My desc")
class Test_baba:
    allure.description("Adding Student Details")
    def test_addStudent_Details(self):
        apiURL="http://thetestingworldapi.com/api/studentsDetails"
        file = open("D:\\Pycharm\\API\\PostRequest.json", "r")

        #Global variables

        global myid
        myid=''
        global json_payload

        #Loading file into the JSON
        json_payload=json.loads(file.read())

        #Making request
        response=requests.post(apiURL, json_payload)

        #Extracting data from respose
        extract_id= jsonpath.jsonpath(response.json(), 'id')
        myid=extract_id[0]
        print("Global id is ", myid)

    allure.description("Getting student details")
    def test_getStudentdata(self):
        apiURL = "http://thetestingworldapi.com/api/studentsDetails/"+str(myid)

        # Making request
        reponse=requests.get(apiURL)

        #Extracting response

        firstname=jsonpath.jsonpath(reponse.json(), 'data.first_name')
        print(firstname[0])

        assert json_payload['first_name'] == firstname[0]

        # print(reponse.text)
    allure.description("Adding tech details")
    def test_addTechincaldetails(self):
        appurl="http://thetestingworldapi.com/api/technicalskills"
        fileaddtech = open("D:\\Pycharm\\API\\addtech.json", "r")
        json_payload=json.loads(fileaddtech.read())
        json_payload['id']= myid
        json_payload['st_id'] = int(myid)
        reponse=requests.post(appurl, json_payload)
        # print(json_payload)

    allure.step("Veifing details")
    def test_getTechincaldetails(self):
        appurl = "http://thetestingworldapi.com/api/technicalskills/"
        reponse=requests.get(appurl)
        std_id= jsonpath.jsonpath(reponse.json(), 'data[*].st_id')
        print(std_id)

        assert str(myid) in std_id
        print("Global id is ", myid)





