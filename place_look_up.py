import json
import urllib
import requests
from urllib import request
import json
import pandas



API_KEY = 'AIzaSyCX_wY-EZ0kDUQ_s1blv-txWWwsankYRG0'
place = 'Daycare+in=Cary+NC'

URL = 'https://maps.googleapis.com/maps/api/place/textsearch/json?query={0}&key={1}'
# Get the feed

#format the query url
query_url = URL.format(place,API_KEY)

r = requests.get(query_url)
data = json.loads(r.text)

i = 0
#print(type(data))
for item in data['results']:
    #result[u'lat']=result[u'location'][u'lat']
    #result[u'lng']=result[u'location'][u'lng']
    #del result[u'location']
    i = i + 1
    #print(i)
    address = 'id={0},name={1}, address={2}, lat={3}, lng={4}, rating={5}'
    print(i, item[u'place_id'],item[u'name'],item[u'formatted_address'],item['geometry']['location']['lat'],item['geometry']['location']['lng'],item[u'rating'])
    #print(address)

#df = pandas.read_json(data)




#print(df)


# Convert it to a Python dictionary
#data = json.loads(r.text)

#print(data)
# Loop through the result.
'''
for item in data['data']['items']:

    print("Video Title: %s" % (item['title']))

    print("Video Category: %s" % (item['category']))

    print("Video ID: %s" % (item['id']))

    print("Video Rating: %f" % (item['rating']))

    print("Embed URL: %s" % (item['player']['default']))

'''
