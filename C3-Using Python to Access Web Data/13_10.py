import urllib.request, urllib.parse, urllib.error
import json

url = input('Enter URL:')
print('Retrieving: ', url)
uh = urllib.request.urlopen(url)
data = uh.read().decode()
js = json.loads(data)
print('Retrieved: ', len(data) , 'characters')

count = 0
sum = 0

for item in js['comments']:
    sum = sum + item['count']
    count += 1

print('Count: ', count)
print('Sum:, ', sum)
