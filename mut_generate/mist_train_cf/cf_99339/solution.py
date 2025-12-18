"""
QUESTION:
Given an XML string with word data, write a function `parse_word_data` that takes this XML string as input and returns the different parts of speech (adjective, verb, adverb, noun) as a dictionary. The XML string will be in the format:
```xml
<word>
    <adjective>...</adjective>
    <verb>...</verb>
    <adverb>...</adverb>
    <noun>...</noun>
</word>
```
Restrictions: Use Python's `xml.etree.ElementTree` module for parsing the XML string.
"""

import xml.etree.ElementTree as ET

def parse_word_data(xml_string):
    """
    This function takes an XML string as input, parses it, and returns a dictionary with the different parts of speech.

    Args:
    xml_string (str): The input XML string.

    Returns:
    dict: A dictionary containing the different parts of speech.
    """
    word_data = ET.fromstring(xml_string)
    return {
        'adjective': word_data.find('adjective').text,
        'verb': word_data.find('verb').text,
        'adverb': word_data.find('adverb').text,
        'noun': word_data.find('noun').text
    }