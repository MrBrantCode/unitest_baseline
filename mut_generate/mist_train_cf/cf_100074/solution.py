"""
QUESTION:
Write a function called `find_longest_consecutive_chain` that takes a sequence of letters as input, where each letter is represented by an XML element `<letter>`. The function should return the longest consecutive chain of letters in alphabetical order and its length. The input sequence is guaranteed to contain only uppercase letters and the letters are not necessarily in order. The function should assume that the input XML data sequence is in the format `<sequence><letter>...</letter>...</sequence>`.
"""

import xml.etree.ElementTree as ET

def find_longest_consecutive_chain(xml_data):
    """
    This function finds the longest consecutive chain of letters in alphabetical order in a given XML data sequence.
    
    Args:
    xml_data (str): The input XML data sequence.
    
    Returns:
    tuple: A tuple containing the longest consecutive chain of letters and its length.
    """
    root = ET.fromstring(xml_data)
    letters = [letter.text for letter in root.findall('letter')]
    letters = sorted(set(letters))  # remove duplicates and sort the list
    
    longest_chain = ""
    current_chain = letters[0]
    
    for i in range(1, len(letters)):
        if ord(letters[i]) == ord(letters[i-1]) + 1:
            current_chain += letters[i]
        else:
            if len(current_chain) > len(longest_chain):
                longest_chain = current_chain
            current_chain = letters[i]
    
    if len(current_chain) > len(longest_chain):
        longest_chain = current_chain
    
    return longest_chain, len(longest_chain)