import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET


while True:
    address = input('Enter location: ')
    if len(address) < 1: break

    
    print('Retrieving', address)
    uh = urllib.request.urlopen(address)

    data = uh.read()
    print('Retrieved', len(data), 'characters')
    tree = ET.fromstring(data)

    counts = tree.findall('.//count')
    print('Count:',len(counts))
    sum=0
    for i in counts:
        a=int(i.text)
        sum = sum+a
    
    print('sum:',sum)
    
    