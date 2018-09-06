from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup

try:
    html = urlopen("https://en.wikipedia.org/wiki/Key_West,_Florida")
except HTTPError as e:
    print(e)
try:
    bsObj = BeautifulSoup(html.read())
except AttributeError as e:
    print(e)
div_ob = bsObj.find('body').findAll('div')[2].findAll('div')[2].findAll('div')[3].findAll('div')[0]
tbody_ob = div_ob.findAll('table')[1]
#print(tbody_ob)

kidList = tbody_ob.contents

print(kidList[19].find('td').findAll('span')[0].find('a').find('span').find('span').findAll('span')[0].get_text())
print(kidList[19].find('td').findAll('span')[0].find('a').find('span').find('span').findAll('span')[1].get_text())

