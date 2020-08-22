# Importing Libraties
import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET

sum = 0
#Asking input the URL of the XML data file
url = input('Enter url: ')
print('Retrieving', url)
uh = urllib.request.urlopen(url)
data = uh.read()
print('Retrieved', len(data), 'characters')

#Transforming the text of the XML file to a tree
tree = ET.fromstring(data)

#Finding all the <comment> tags and putting them into a list
lst = tree.findall('.//count')

print('Count:', len(lst))

for item in lst:
    sum =sum + int(item.text)
print('Sum:', sum)
