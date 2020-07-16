import urllib.request as UR
import xml.etree.ElementTree as ET

url = input('Enter location: ')
# 'http://python-data.dr-chuck.net/comments_42.xml'

total_number = 0
sum = 0

print('Retrieving', url)
xml = UR.urlopen(url).read()
print('Retrieved', len(xml), 'characters')

tr = ET.fromstring(xml)
count = tr.findall('.//count')
for item in count:
    sum += int(item.text)
    total_number += 1

print('Count:', total_number)
print('Sum:', sum)
