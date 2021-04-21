import requests
import json
import jsonpath
import allure
import logging


class api_calls():
    def addStudent_details(self):
        global file
        global endpoint
        global payloadIn_json

        endpoint = "http://thetestingworldapi.com/"
        file = open("C:\\Users\\ovonel\\PycharmProjects\\pythonProject8\\utilities\\request.json", "r")


        #Sending payload to endpoint
        post_studentEndpoint= endpoint+"api/studentsDetails"
        payloadIn_json=json.loads(file.read())

        response=requests.post(post_studentEndpoint, data=payloadIn_json)

        print("Status of post is", response.status_code)

        #Validating respose code
        assert 201==response.status_code

        #Extracting the dynamic id >> Saving into Global variable to use it further
        ids=jsonpath.jsonpath(response.json(), 'id')
        global myid
        myid=ids[0]
        print("My dynamic id is", myid)

    @allure.title("Verfy user is able to get added student details")
    def getStudent_details(self):
        get_studentEndpoint = endpoint+'api/studentsDetails/'+str(myid)
        respose=requests.get(get_studentEndpoint)

        #Checking response code
        assert 200 == respose.status_code

        #Validating the id
        #Validating first name
        #validating Last name
        whole_response = jsonpath.jsonpath(respose.json(), 'data[*]')
        assert payloadIn_json['first_name'] and payloadIn_json['last_name'] and myid in whole_response
        allure.dynamic.description("Testing........with......"+ str(myid))

    @allure.title("getting tech details of student and validating no duplicate id is already existing")
    def getTechDetails_negative(self):
        endppoint = endpoint +'api/technicalskills/'
        responce = requests.get(endppoint)

        # Extractinng all st_id's
        # Cheching 'myid' in not available in the list st_id list
        std_id = jsonpath.jsonpath(responce.json(), 'data[*].st_id')
        assert str(myid) not in std_id

    @allure.title("Verfying adding Technical Skill to student data")
    def addingTechDetails(self):
        endppoint= endpoint+'api/technicalskills/'
        file=open("C:\\Users\\ovonel\\PycharmProjects\\pythonProject8\\utilities\\addTechDetails_request.json", "r")

        #Loading the file
        #We are removing sample id of respose with latest id
        json_payload=json.loads(file.read())
        json_payload['id']=int(myid)
        json_payload['st_id']=str(myid)

        #Sending request
        response=requests.post(endppoint, data=json_payload)
        assert 201== response.status_code

    @allure.title("fetching added technical details with dynamic id")
    def getTechDetails_positive(self):
        endppoint= endpoint+'api/technicalskills/'
        responce=requests.get(endppoint)

        #Extractinng all st_id's
        #Cheching 'myid' in st_id list
        std_id=jsonpath.jsonpath(responce.json(), 'data[*].st_id')
        print(myid)
        assert str(myid) in std_id










