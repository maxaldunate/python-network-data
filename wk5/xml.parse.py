import xml.etree.ElementTree as ET

xml_data = '''
<person>
    <name>Max</name>
    <phone type="intl">
        +34 777 888 999
    </phone>
    <email hide="yes" />
</person>
'''

tree = ET.fromstring(xml_data)
print('Name:', tree.find('name').text)
print('Attr:', tree.find('email').get('hide'))

