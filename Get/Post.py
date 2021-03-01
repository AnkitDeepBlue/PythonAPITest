import requests
import json
import jsonpath
import pytest

from Get.Repos.samples import noteBook


@pytest.fixture(scope="class")
def setup():
    global url
    global file
    url= noteBook.url
    file= noteBook.file

def test_apiCall(setup):

    #Reading file
    read=file.read()

    #Loadind file in json
    json_input_load= json.loads(read
                                )

    #making Post and storing respose
    response=requests.put(url, json_input_load)
    assert 200== response.status_code

    #fatchiing respose headers
    # print(response.headers)

    #Fatching respose main data

    responseJson= json.loads(response.text)
    mainrespose=jsonpath.jsonpath(responseJson, 'job')
    assert mainrespose[0]== json_input_load['job']

    print(mainrespose[0])