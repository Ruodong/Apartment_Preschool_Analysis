def print_gmap_address(index,item):
    print(index,
      item.get(u'name',''),
      item.get(u'formatted_address'),
      item.get(u'rating',''))

def print_gmap_dict_address(index,apartment,direction):
    print('---',index,
          apartment.get(u'name'),
          apartment.get(u'vicinity'),
          apartment.get(u'rating'),
          direction.get(u'duration').get('text'),
          direction.get(u'distance').get('text')
          )

def get_location(loc):
    return str(loc.get('geometry').get('location').get('lat')) + ',' + str(loc.get('geometry').get('location').get('lng'))



