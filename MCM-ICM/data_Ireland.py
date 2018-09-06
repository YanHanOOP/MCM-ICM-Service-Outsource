from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup
import googlemaps


gmaps = googlemaps.Client(key='AIzaSyCsmvCrWptWquVNyUG76Wsu0qcCfoxxQeI')

cityList = [['Dublin,Ireland','Dundalk,Ireland'],
            ['Blanchardstown,Ireland','Ashbourne,Ireland'],
            ['Clonee,Ireland','Dun Buinne,Ireland'],
            ['Lucan,Ireland','Kinnegad,Ireland'],
            ['Kinnegad,Ireland','Ballinasloe,Ireland'],
            ['Naas,Ireland','Limerick,Ireland'],
            ['Cullahill,Ireland','Cork,Ireland'],
            ['Newbridge,Ireland','Kilkenny,Ireland'],
            ['Shankill,Ireland','Gorey,Ireland'],
            ['Shanno,Ireland','Gort,Ireland'],
            ['Limerick,Ireland','Patrickswell,Ireland'],
            ['Port,Ireland','Loughlinstown,Ireland']
            ]

length = len(cityList)
i=0
while(i < length):
    start_place = cityList[i][0]
    stop_place = cityList[i][1]
    start_result = gmaps.geocode(start_place)
    startLat = start_result[0]['geometry']['location']['lat']
    startLng = start_result[0]['geometry']['location']['lng']

    stop_result = gmaps.geocode(stop_place)
    stopLat = stop_result[0]['geometry']['location']['lat']
    stopLng = stop_result[0]['geometry']['location']['lng']
    print(start_place,';',startLat,';',startLng,';',stop_place,';',stopLat,';',stopLng)
    i = i + 1
