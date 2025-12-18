"""
QUESTION:
Implement a function `find_xml_id(xml_data)` to extract the value of the 'id' key from the given XML string `xml_data`. The 'id' value should be returned as an integer. You must implement your own XML parser without using any XML parsing libraries or functions. The XML data is assumed to have a simple format with double quotes around attribute values and no nested tags or complex structures.
"""

def find_xml_id(xml_data):
    # Find the starting position of the 'id' key
    id_start = xml_data.find('id="')

    if id_start == -1:
        return None  # 'id' key not found

    # Find the ending position of the 'id' value
    id_end = xml_data.find('"', id_start + 4)

    if id_end == -1:
        return None  # Unable to find closing double quote

    # Extract the 'id' value
    id_value = xml_data[id_start + 4:id_end]

    try:
        # Convert the 'id' value to an integer and return
        return int(id_value)
    except ValueError:
        return None  # 'id' value is not a valid integer