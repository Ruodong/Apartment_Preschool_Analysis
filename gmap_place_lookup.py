import googlemaps
import time
import util as ut
import zillow_rental as zr

gmaps = googlemaps.Client(key='AIzaSyCX_wY-EZ0kDUQ_s1blv-txWWwsankYRG0')
gmap_dirt = googlemaps.Client(key='AIzaSyDz6u-ORWIwTGHaAVUZvoQ2VNUO-KB4qwM')


CITY = 'cary'
STATE = 'NC'

query_string = 'preschool,daycare in ' + CITY + ', ' + STATE
# Geocoding an address
daycare_result = gmaps.places(query=query_string)
i = 0

apartment_result = []
apartment = []
apartment_dict_result = []

while i <= 60:
    for item in daycare_result['results']:
        i = i + 1
        ut.print_gmap_address(i,item)
        j = 0
        time.sleep(0.1)
        org_loc = ut.get_location(item)
        apartment_result = gmaps.places_nearby(location=org_loc,keyword='apartment',radius=1000)
        for apartment in apartment_result['results']:
            dest_loc = ut.get_location(apartment)
            apartment_dict_result = gmap_dirt.directions(origin=org_loc,
                                                          destination=dest_loc,
                                                          mode='walking')
            for direction in apartment_dict_result[0]['legs']:
                if direction.get(u'duration').get('value') /60 <= 20:
                    j = j + 1

                    ut.print_gmap_dict_address(j,apartment,direction)

                    zr.print_zillow_price(apartment.get(u'vicinity'),'cary','NC')
    token = daycare_result.get(u'next_page_token',None)
    if token is None:
        break
    else:
        daycare_result = gmaps.places(query=query_string,page_token=token)




