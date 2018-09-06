from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup
import googlemaps


gmaps = googlemaps.Client(key='AIzaSyCsmvCrWptWquVNyUG76Wsu0qcCfoxxQeI')


try:
    html = urlopen("https://en.wikipedia.org/wiki/List_of_United_States_Numbered_Highways")
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
i = 3
while(kidList[i] is not None):
    startList = kidList[i].findAll('td')[2].findAll('a')
    startLength = len(startList)
    if(startLength > 1):
        startPlace = kidList[i].findAll('td')[2].findAll('a')[startLength-1].get_text()
        startRef = kidList[i].findAll('td')[2].findAll('a')[startLength-1].get('href')
        #startPlace,Latitude,Longitude
        start_result = gmaps.geocode(startPlace)
        startLat = start_result[0]['geometry']['location']['lat']
        startLng = start_result[0]['geometry']['location']['lng']
    else:
        startPlace = kidList[i].findAll('td')[2].findAll('a')[0].get_text()
        startRef = kidList[i].findAll('td')[2].findAll('a')[0].get('href')
        #startPlace,Latitude,Longitude
        start_result = gmaps.geocode(startPlace)
        startLat = start_result[0]['geometry']['location']['lat']
        startLng = start_result[0]['geometry']['location']['lng']

    stopList = kidList[i].findAll('td')[3].findAll('a')
    stopLength = len(stopList)
    if(stopLength > 1):
        stopPlace = kidList[i].findAll('td')[3].findAll('a')[stopLength-1].get_text()
        stopRef = kidList[i].findAll('td')[3].findAll('a')[stopLength-1].get('href')
        #stopPlace,Latitude,Longitude
        stop_result = gmaps.geocode(stopPlace)
        stopLat = stop_result[0]['geometry']['location']['lat']
        stopLng = stop_result[0]['geometry']['location']['lng']
    else:
        stopPlace = kidList[i].findAll('td')[3].findAll('a')[0].get_text()
        stopRef = kidList[i].findAll('td')[3].findAll('a')[0].get('href')
        #stopPlace,Latitude,Longitude
        stop_result = gmaps.geocode(stopPlace)
        stopLat = stop_result[0]['geometry']['location']['lat']
        stopLng = stop_result[0]['geometry']['location']['lng']

    print(startPlace,';',startLat,';',startLng,';',stopPlace,';',stopLat,';',stopLng)
    i = i + 2
#print(kidList[3])#+2

