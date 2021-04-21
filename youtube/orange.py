import requests
import json
import jsonpath
import allure
import logging
from bs4 import BeautifulSoup

import re

session=requests.session()

response=session.get("https://opensource-demo.orangehrmlive.com")

soup=BeautifulSoup(response.text, 'lxml')
token=soup.select("#csrf_token")[0].get("value")
print(token)

pattern=re.compile(r'<input type="hidden" name="_csrf_token" value="(.+)?" id="csrf_token"')

token_b=re.search(pattern, response.text)
print(token_b.group(1))

data={
"actionID":"",
"hdnUserTimeZoneOffset": "5.5",
"_csrf_token": token_b,
"txtUsername": "Admin",
"txtPassword": "admin",
"Submit": "LOGIN"
}
url_post="https://opensource-demo.orangehrmlive.com/index.php/auth/validateCredentials"
response=session.post(url_post, data=data)

print(response.text)

assert "log out" in response.text