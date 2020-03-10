import xml.etree.ElementTree as et
    tree = et.parse('data.xml')
    root = tree.getroot()
print(root)


import json
with open('data.json') as f:
    data = json.load(f)
print(data)


#masih gagal