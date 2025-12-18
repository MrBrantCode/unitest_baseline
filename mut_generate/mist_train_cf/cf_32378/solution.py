"""
QUESTION:
Write a function called `extract_amendments` that takes a string `speech` as input. The function should extract the names of the political parties and the proposed amendments to the bill's sections from the input string and return them as a dictionary with two keys: "parties" (a list of strings representing the names of the political parties that submitted a dissenting opinion) and "amendments" (a list of strings representing the proposed amendments to specific sections of the bill). The input string may contain multiple occurrences of political party names and references to bill sections, and the proposed amendments are indicated by the intention to maintain the sections unchanged.
"""

import re

def extract_amendments(speech):
    parties = re.findall(r'\b(?:vihreät|vasemmistoliitto|RKP)\b', speech)
    amendments = re.findall(r'\d+\s§', speech)
    return {"parties": parties, "amendments": amendments}