"""
QUESTION:
Write a function `extract_employee_ids` that takes an XML string as input and returns a list of IDs of all employees. The XML string is in the format: 
```xml
<data>
  <employee>
    <id>employee_id</id>
    <name>employee_name</name>
    <department>department_name</department>
  </employee>
  ...
</data>
```
Use the `xml.etree.ElementTree` module to parse the XML data.
"""

import xml.etree.ElementTree as ET

def extract_employee_ids(xml_string):
    """
    Extracts employee IDs from an XML string.

    Args:
        xml_string (str): The input XML string.

    Returns:
        list: A list of employee IDs.
    """
    root = ET.fromstring(xml_string)
    return [employee.find('id').text for employee in root.findall('employee')]