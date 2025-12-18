"""
QUESTION:
Write a function `etree_to_dict(t)` that converts an XML ElementTree object `t` into a dictionary. The function should recursively handle nested elements and attributes in the XML syntax, and efficiently handle memory usage for large XML documents. The function should return a dictionary that can be used to generate a YAML representation of the XML. 

Restrictions: The input XML document may contain nested elements and attributes, and the solution must process the XML tree node by node without holding the whole document in memory at once.
"""

import xml.etree.ElementTree as ET

def etree_to_dict(t):
    d = {t.tag: {} if t.attrib else None}
    children = list(t)
    if children:
        dd = {}
        for dc in map(etree_to_dict, children):
            for k, v in dc.items():
                try:
                    dd[k].append(v)
                except KeyError:
                    dd[k] = [v]
        d = {t.tag: {k: v[0] if len(v) == 1 else v for k, v in dd.items()}}
    if t.attrib:
        d[t.tag].update(('@' + k, v) for k, v in t.attrib.items())
    if t.text:
        text = t.text.strip()
        if children or t.attrib:
            if text:
                d[t.tag]['#text'] = text
        else:
            d[t.tag] = text
    return d