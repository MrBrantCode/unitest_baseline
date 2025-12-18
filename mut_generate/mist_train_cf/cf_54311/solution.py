"""
QUESTION:
Write a function named `extract_namespaces` that takes a file as an input, extracts all namespaces from the given XML document, and returns a dictionary containing these namespaces with their corresponding URIs. The function should handle possible exceptions and edge cases effectively, including XML parsing errors, file not found errors, and any other unexpected errors. The function should only include namespaces that are used in the XML document tags.
"""

import xml.etree.ElementTree as ET

def extract_namespaces(file):
    try:
        document = ET.parse(file)
        root = document.getroot()
        namespaces = {}
        for elem in root.iter():
            if '}' in elem.tag:
                ns, tag = elem.tag.split('}', 1)
                if ns not in namespaces:
                    namespaces[ns.strip('{}')] = elem.tag.split('}')[0].strip('{}')
        return namespaces
    except ET.ParseError:
        print("File could not be parsed as XML.")
    except FileNotFoundError:
        print("File does not exist.")
    except Exception as e:
        print("An unexpected error occurred:", e)