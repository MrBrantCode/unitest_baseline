"""
QUESTION:
Write a function `extract_title_and_author(xml_data)` that uses regular expressions to extract the title and author from a given XML string. The XML string is in the format `<book><title>title</title><author>author</author></book>`. The function should return the extracted title and author as strings.
"""

import re

def extract_title_and_author(xml_data):
    """
    Extracts the title and author from a given XML string using regular expressions.

    Args:
        xml_data (str): The XML string to extract from.

    Returns:
        tuple: A tuple containing the extracted title and author as strings.
    """
    title = re.search('<title>(.*?)</title>', xml_data).group(1)
    author = re.search('<author>(.*?)</author>', xml_data).group(1)
    return title, author