import requests
from bs4 import BeautifulSoup

# get html
res = requests.get('https://www.yahoo.co.jp/')

# add html to perser
soup = BeautifulSoup(res.text,'html.parser')

# get dom text by class name
values = soup.select_one('.t_jb9bKlgIcajcRS2hZAP').findAll(text=True)
print(values)