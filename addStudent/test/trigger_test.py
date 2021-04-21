import requests
import json
import jsonpath
import allure
import logging
import pytest
from addStudent.apiStudents import api_calls


@allure.title("Verfy user is able to add student details")
class Test_myapi(api_calls):

    @allure.title("Adding student details")
    def test_add_student_details(self):
        api_calls.addStudent_details(self)

    @allure.title("Verifing added student details")
    def test_added_student_details(self):
        api_calls.getStudent_details(self)

    @pytest.mark.skip
    @allure.title("Verifing technical details-Negetive testing")
    def test_get_technical_details_negetive(self):
        api_calls.getTechDetails_negative(self)

    @pytest.mark.skip
    @allure.title("Adding technical details")
    def test_add_technical_details(self):
        api_calls.addStudent_details(self)

    @pytest.mark.skip
    @allure.title("Verifing technical details-Postive testing")
    def test_get_technical_details_positive(self):
        api_calls.getTechDetails_positive(self)








        # obj=apiEndToEnd()
        # obj.addStudent_details()
        # obj.test_getStudent_details()
        # obj.test_getTechDetails_negative()
        # obj.test_addingTechDetails()
        # obj.test_getTechDetails_positive()



