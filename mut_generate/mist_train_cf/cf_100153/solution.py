"""
QUESTION:
Write a function named `extract_ids` that takes an XML string in the given format as input and returns a list of IDs of all employees. The XML string is in the format:
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
Restrictions: Use the `xml.etree.ElementTree` module.
"""

import xml.etree.ElementTree as ET

def extract_ids(xml_string):
    """
    Extracts and returns a list of IDs from the given XML string.

    Args:
        xml_string (str): The input XML string.

    Returns:
        list: A list of IDs of all employees.
    """
    root = ET.fromstring(xml_string)
    ids = []
    for employee in root.findall('employee'):
        id = employee.find('id').text
        ids.append(id)
    return ids