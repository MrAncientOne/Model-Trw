import requests
import os
from bs4 import BeautifulSoup

response=requests.get("https://www.propleaf.com/localities-in-chennai")
response=BeautifulSoup(response.content,'html5lib')
response=response.find_all('li',attrs={'class':'col-lg-3 col-md-4 col-6'})
with open("file.txt", "w") as f:
    for i in response:
        check=i.find('a')
        f.write(f"{check.get_text()}\n")
#print(response.name)