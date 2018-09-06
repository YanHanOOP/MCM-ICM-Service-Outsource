import urllib  
from urllib.request import urlopen  
import json  
  
def getGeoForAddress(address):  
    addressUrl = "http://maps.googleapis.com/maps/api/geocode/json?address=" + address  
    addressUrlQuote = urllib.parse.quote(addressUrl, ':?=/')  
    response = urlopen(addressUrlQuote).read().decode('utf-8')  
    responseJson = json.loads(response)  

    lat = responseJson.get('results')[0]['geometry']['location']['lat']  
    lng = responseJson.get('results')[0]['geometry']['location']['lng']  
    print(address + ': %f, %f'  %(lat, lng))  
    return [lat, lng]  

getGeoForAddress('South Waverly, PA')
getGeoForAddress('Boardman, OR')
getGeoForAddress('Ilwaco, WA')
