"""
QUESTION:
Write a function `extractCharset` that takes a string representing an HTML meta tag as input and returns the value of the "charset" attribute. The input string is in the format `<meta charset="value">`, where "value" represents the character encoding, and the "charset" attribute is always present.
"""

def extractCharset(meta_tag):
    start_index = meta_tag.find('charset="') + len('charset="')
    end_index = meta_tag.find('"', start_index)
    return meta_tag[start_index:end_index]