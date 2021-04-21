import requests
from bs4 import BeautifulSoup
import re

session=requests.Session()

reponse=session.get('https://opensource-demo.orangehrmlive.com/')

soup=BeautifulSoup(reponse.text, 'lxml')
token=soup.select('#csrf_token')[0].get('value')
print(token)

pattern=re.compile(r'<input type="hidden" name="_csrf_token" value="(.+)?" id="csrf_token"')
token_new=re.search(pattern, reponse.text)
print(token_new.group(1))