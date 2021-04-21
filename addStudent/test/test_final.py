import requests
import json
import jsonpath
import pytest
import allure
import logging

from addStudent.apiStudents import apiEndToEnd


class Test_student_Api:

    call=apiEndToEnd()

    call.addStudent_details()
    call.test_getStudent_details()
    call.test_getTechDetails_negative()
    call.test_addingTechDetails()
    call.test_getTechDetails_positive()
