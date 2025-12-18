"""
QUESTION:
Extract the title and author from a given XML string using regular expressions in Python. 

The function should take a string representing the XML content as input and return a tuple containing the title and author. The XML string will be in the format `<book><title>title</title><author>author</author></book>`.
"""

import re

def extract_info(xml_string):
    """
    Extracts title and author from a given XML string.

    Args:
    xml_string (str): A string representing the XML content.

    Returns:
    tuple: A tuple containing the title and author.
    """
    title = re.search(r'<title>(.*?)</title>', xml_string)
    author = re.search(r'<author>(.*?)</author>', xml_string)
    
    if title and author:
        return title.group(1), author.group(1)
    else:
        return None