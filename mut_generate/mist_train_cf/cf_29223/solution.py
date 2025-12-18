"""
QUESTION:
Write a function `parseIl2
"""

import re

def parseIl2Sizes(code_snippet):
    result = {}
    match = re.search(r'extern const Il2CppIl2CppTypeDefinitionSizes (\w+) = { (.*), (.*), (.+), (.+) };', code_snippet)
    if match:
        result["name"] = match.group(1)
        result["size"] = match.group(2)
        result["type"] = match.group(3)
    return result