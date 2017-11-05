from urllib.request import urlopen
import ssl
import xml.etree.ElementTree as ET

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = 'http://py4e-data.dr-chuck.net/comments_40679.xml'
xml_data = urlopen(url, context=ctx).read()
xml_tree = ET.fromstring(xml_data)
lst = xml_tree.findall('comments/comment/count')
print('Comments counts:', len(lst))

sum = 0
for comment in lst:
    sum = sum + int(comment.text)

print()
print('Sum: ', sum)
