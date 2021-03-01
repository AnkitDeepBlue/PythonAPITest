import pytest

from Get.Repos.samples import noteBook

pytest.fixture
import time
import pytest
import requests
import json
import jsonpath

@pytest.fixture(scope="class")
def setup():
 url= noteBook.url
 file= noteBook.file


