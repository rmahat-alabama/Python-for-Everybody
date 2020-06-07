import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl
import urllib
import json

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


# serviceurl = 'http://maps.googleapis.com/maps/api/geocode/json?'
serviceurl = 'http://python-data.dr-chuck.net/geojson?'
while True:
    location = input('Enter location: ')
    if len(location) < 1 : break
    url = serviceurl + urllib.urlencode({'sensor':'false', 'address': location})
    print ('Retrieving', url)
    uh = urllib.request.urlopen(url, context=ctx)
    data = uh.read()
    print ('Retrieved',len(data),'characters')
    try:
        js = json.loads(str(data))
    except:
        js = None
    print ('Place ID ', js["results"][0]["place_id"])
