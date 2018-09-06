import googlemaps


gmaps = googlemaps.Client(key='AIzaSyCsmvCrWptWquVNyUG76Wsu0qcCfoxxQeI')


geocode_result = gmaps.geocode('Ilwaco, WA')

#print(geocode_result[0])
#print(type(geocode_result[0]))
print(geocode_result[0]['geometry']['location']['lat'])
print(geocode_result[0]['geometry']['location']['lng'])
