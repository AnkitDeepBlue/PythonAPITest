import requests
import json
import jsonpath
import pytest
import allure


class Test_apiEndToEnd():


    def mysample(self):
        print("baba")

    @allure.title("Verfy user is able to add student details")
    @allure.description("Adding Student Details")
    @allure.step("")
    def test_addStudent_details(self):

        global file
        global endpoint
        global payloadIn_json
        endpoint = "http://thetestingworldapi.com/"
        file = open("C:\\Users\\ovonel\\PycharmProjects\\pythonProject8\\utilities\\request.json", "r")
        # Sending payload to endpoint
        post_studentEndpoint= endpoint+"api/studentsDetails"
        payloadIn_json=json.loads(file.read())
        response=requests.post(post_studentEndpoint, payloadIn_json)
        print("Status of post is", response.status_code)

        #Validating respose code
        assert 201==response.status_code


        #Extracting the id >> Saving into Global variable to use it further
        ids=jsonpath.jsonpath(response.json(), 'id')
        global myid
        myid=ids[0]

    @allure.title("Verfy user is able to get added student details")
    @allure.description("getting student details")
    @allure.step("verfying the data with")
    def test_getStudent_details(self):

        get_studentEndpoint = endpoint+'api/studentsDetails/'+str(myid)
        respose=requests.get(get_studentEndpoint)

        #Checking response code
        assert 200 == respose.status_code

        #Validating the id
        #Validating first name
        # validating Last name
        whole_response = jsonpath.jsonpath(respose.json(), 'data[*]')
        assert payloadIn_json['first_name'] and payloadIn_json['last_name'] and myid in whole_response
        print(myid)
        allure.dynamic.description("Testing........with......"+ str(myid))

    @allure.description("getting tech details of student and validating no duplicate id is already existing")
    def test_getTechDetails_negative(self):
        endppoint = endpoint + 'api/technicalskills/'

        responce = requests.get(endppoint)

        # Extractinng all st_id's
        # Cheching 'myid' in not available in the list st_id list
        std_id = jsonpath.jsonpath(responce.json(), 'data[*].st_id')
        assert str(myid) not in std_id

    @allure.title("Verfying adding Technical Skill to student data")
    @allure.description("Adding Technical Skill to student data with dynamic id")
    def test_addingTechDetails(self):
        endppoint= endpoint+'api/technicalskills/'
        file=open("C:\\Users\\ovonel\\PycharmProjects\\pythonProject8\\utilities\\addTechDetails_request.json", "r")

        #Loading the file
        #We are removing sample id of respose with latest id
        json_payload=json.loads(file.read())
        json_payload['id']=int(myid)
        json_payload['st_id']=str(myid)

        response=requests.post(endppoint, json_payload)
        assert 200== response.status_code

    @allure.title("fetching added technical details with dynamic id")
    @allure.description("verfying technical details")
    def test_getTechDetails_positive(self):
        endppoint= endpoint+'api/technicalskills/'

        responce=requests.get(endppoint)

        #Extractinng all st_id's
        #Cheching 'myid' in st_id list
        std_id=jsonpath.jsonpath(responce.json(), 'data[*].st_id')
        assert str(myid) in std_id











