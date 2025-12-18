"""
QUESTION:
Write a function named `parse_word_xml` that takes an XML string representing a word with different parts of speech (adjective, verb, adverb, and noun) and returns a dictionary containing the word's parts of speech. The XML string is in the format: `<word><adjective>...</adjective><verb>...</verb><adverb>...</adverb><noun>...</noun></word>`. The function should use the `xml.etree.ElementTree` module to parse the XML string.
"""

import xml.etree.ElementTree as ET

def parse_word_xml(xml_string):
    """
    Parse an XML string representing a word with different parts of speech.

    Args:
    xml_string (str): The XML string to parse.

    Returns:
    dict: A dictionary containing the word's parts of speech.
    """
    word_data = ET.fromstring(xml_string)
    adjective = word_data.find('adjective').text
    verb = word_data.find('verb').text
    adverb = word_data.find('adverb').text
    noun = word_data.find('noun').text
    
    return {
        'adjective': adjective,
        'verb': verb,
        'adverb': adverb,
        'noun': noun
    }