from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl, re

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = 'http://py4e-data.dr-chuck.net/known_by_Alexis.html'
resultName = ''

for x in range(0, 7):
    html = urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, "html.parser")
    tags = soup('a')
    currentTag = tags[17]
    url = currentTag.get('href', None)
    resultName = currentTag.contents[0]

print(resultName)