"""
QUESTION:
You need to implement a function `parse_xml_input(xml_input: str) -> dict` that takes a string `xml_input` representing the XML configuration as input and returns a dictionary containing the precision and dimensions of the ports. The function should extract the precision and dimensions of each port specified in the XML input and store them in the dictionary with the port ID as the key and a tuple of precision and dimensions as the value. The XML input will always follow a specific format where the precision attribute of the port element will be one of "FP32", "FP64", or "INT8", and the dimensions of the port will be represented by the <dim> tag inside the <port> element.
"""

import xml.etree.ElementTree as ET

def parse_xml_input(xml_input: str) -> dict:
    result = {}
    root = ET.fromstring(xml_input)
    for port in root.findall('port'):
        port_id = port.get('id')
        precision = port.get('precision')
        dim = int(port.find('dim').text)
        result[port_id] = (precision, dim)
    return result