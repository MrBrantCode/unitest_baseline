"""
QUESTION:
Implement a function `convert_xml_to_dict(xml_string)` that takes a string of XML as input and returns a list of dictionaries. The function should validate the XML string to ensure it has the required 'person', 'name', and 'age' tags, and handle any errors due to mismatched or missing tags. Do not use any external libraries for XML parsing.
"""

def convert_xml_to_dict(xml_string):
    def validate_tag(tag_name):
        open_tag = '<' + tag_name + '>'
        close_tag = '</' + tag_name + '>'
        open_tag_occurrences = xml_string.count(open_tag) 
        close_tag_occurrences = xml_string.count(close_tag)
        if open_tag_occurrences != close_tag_occurrences:
            raise Exception('Invalid XML: Mismatched ' + tag_name + ' tags')
        if open_tag_occurrences == 0:
            raise Exception('Invalid XML: Missing ' + tag_name + ' tags')

    def get_values_for_tag(tag_name):
        open_tag = '<' + tag_name + '>'
        close_tag = '</' + tag_name + '>'
        start = xml_string.find(open_tag)
        values = []
        while start != -1:
            start += len(open_tag)
            end = xml_string.find(close_tag, start)
            values.append(xml_string[start:end].strip())
            start = xml_string.find(open_tag, end)
        return values

    validate_tag('person')
    validate_tag('name')
    validate_tag('age')
    names = get_values_for_tag('name')
    ages = get_values_for_tag('age')
    return [{'name': n, 'age': a} for n, a in zip(names, ages)]