# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

count =0
sum =0

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

#Asking user to input the URL
url = input('Enter - ')
html = urlopen(url, context=ctx).read()

#Creating an organized string(soup) with Beautiful Soup
soup = BeautifulSoup(html, "html.parser")

# Retrieve all of the anchor tags
tags = soup('span')
for tag in tags:
    num = tag.contents[0]
    #print('Contents:', tag.contents[0])
    num =int(num)
    sum =sum + num
    count = count +1
# printing the results
print(sum)
print(count)
