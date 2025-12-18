"""
QUESTION:
Write a function `parse_xml_to_dict` that takes an XML string as input, parses the XML data, and returns a dictionary where the country name is the key. The dictionary value should be another dictionary with keys for rank, year, gdppc, and neighbors. The value for neighbors should be a list of dictionaries where each dictionary contains the name of the neighbor country and its location direction. The XML data is assumed to have the following structure: 
```xml
<data>
  <country name="country_name">
    <rank>rank_value</rank>
    <year>year_value</year>
    <gdppc>gdppc_value</gdppc>
    <neighbor name="neighbor_name" direction="direction"/>
  </country>
</data>
```
"""

import xml.etree.ElementTree as ET

def parse_xml_to_dict(xml_data):
    root = ET.fromstring(xml_data)
    country_dict = {}
    for country in root.findall('country'):
        name = country.get('name')
        rank = country.find('rank').text
        year = country.find('year').text
        gdppc = country.find('gdppc').text
        neighbors = [{"name": n.get('name'), "direction": n.get('direction')} for n in country.findall('neighbor')]
        country_dict[name] = {"rank": rank, "year": year, "gdppc": gdppc, "neighbors": neighbors}
    return country_dict