import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl
import urllib
import json

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


counts = list()
while True:
    url = input('Enter location: ')
    if len(url) < 1 : break
    print ('Retrieving', url)
    uh = urllib.request.urlopen(url, context=ctx)
    data = uh.read()
    print ('Retrieved',len(data),'characters')
    try:
        js = json.loads(data)
    except:
        js = None
    comments = js['comments']
    for comment in comments:
        counts.append(comment['count'])
    print ('Count', len(comments))
    print ('Sum', sum(counts))
