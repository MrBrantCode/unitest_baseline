"""
QUESTION:
Create a function to parse the given XML structure and implement search and filter functions. The XML structure includes a list of persons with attributes such as name, age, family relations, and job details.

The XML structure is as follows: 
<people>
  <person>
    <name>name</name>
    <age>age</age>
    <family>
      <parent>parent_name</parent>
      <child>child_name</child>
    </family>
    <job>
      <title>job_title</title>
      <company>company_name</company>
    </job>
  </person>
</people>

Implement two functions: search(term) and filter(criteria). The search function should return all persons whose attributes match the search term. The filter function should return only those persons whose attributes fulfill the filter criteria. The filter criteria should be a dictionary of attributes.
"""

import xml.etree.ElementTree as ET

def entrance(xml_string):
    root = ET.fromstring(xml_string)
    persons = []

    for person in root.findall('person'):
        data = {}

        data['name'] = person.find('name').text
        data['age'] = int(person.find('age').text)

        family = person.find('family')
        if family is not None:
            data['family'] = {}
            for member in family:
                data['family'][member.tag] = member.text

        job = person.find('job')
        if job is not None:
            data['job'] = {}
            for detail in job:
                data['job'][detail.tag] = detail.text
        
        persons.append(data)

    def search(term):
        result = [p for p in persons if term in str(p.values())]
        return result

    def filter(criteria):
        result = [p for p in persons if all(str(item) in str(p.items()) for item in criteria.items())]
        return result

    return search, filter