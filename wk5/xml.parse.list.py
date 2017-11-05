import xml.etree.ElementTree as ET

xml_data = '''
<stuff>
    <users>
        <user x="2">
            <id>001</id>
            <name>Max</name>
        </user>
        <user x="7">
            <id>009</id>
            <name>Brent</name>
        </user>
    </users>
</stuff>
'''

stuff = ET.fromstring(xml_data)
lst = stuff.findall('users/user')
print('User count:', len(lst))

for user in lst:
    print()
    print('Name', user.find('name').text)
    print('Id  ', user.find('id').text)
    print('Attr', user.get('x'))
