from bs4 import BeautifulSoup
import urllib.request

ZILLOW_KEY = 'X1-ZWz1fnj6kaw0ln_7ew1d'


def print_zillow_price(address,city,state):

    address = address.replace(', Cary','')

    query_url = 'http://www.zillow.com/webservice/GetSearchResults.htm?zws-id={0}&address={1}&citystatezip={2}'
    query_url= query_url.format(ZILLOW_KEY,address,city + ',' +state)

    r = urllib.request.urlopen(query_url)
    doc = BeautifulSoup(r,'xml')
    for item in doc.findall('message'):
        print(item)
