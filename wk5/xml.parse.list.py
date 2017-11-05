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

for item in lst:
    print()
    print('Name', item.find('name').text)
    print('Id  ', item.find('id').text)
    print('Attr', item.get('x'))
