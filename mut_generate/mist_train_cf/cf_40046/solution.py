"""
QUESTION:
Implement a function `parse_backend_config(xml_config: str) -> Dict[str, Dict[str, Union[str, Dict[str, str]]]]` that parses the provided XML configuration string and returns a dictionary where each key is the backend id and the corresponding value is a dictionary containing the backend attributes and child elements as key-value pairs. The XML configuration string is expected to have a root element named 'backends' with multiple child elements named 'backend', each containing attributes 'id', 'type', 'weight', and 'store_by', as well as child elements 'files_dir' and 'extra_dir'.
"""

import xml.etree.ElementTree as ET
from typing import Dict, Union

def parse_backend_config(xml_config: str) -> Dict[str, Dict[str, Union[str, Dict[str, str]]]]:
    backend_config = {}
    root = ET.fromstring(xml_config)
    for backend in root.findall('backend'):
        backend_id = backend.attrib['id']
        backend_details = {
            'type': backend.attrib['type'],
            'weight': backend.attrib['weight'],
            'store_by': backend.attrib['store_by']
        }
        files_dir = backend.find('files_dir').attrib
        extra_dirs = {extra_dir.attrib['type']: extra_dir.attrib for extra_dir in backend.findall('extra_dir')}
        backend_details['files_dir'] = files_dir
        backend_details['extra_dir'] = extra_dirs
        backend_config[backend_id] = backend_details
    return backend_config