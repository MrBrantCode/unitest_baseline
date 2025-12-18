"""
QUESTION:
Write a function `parseXDR` that takes a string `xdr_source` representing a simplified XDR source and returns a dictionary where the keys are the structure names and the values are lists of field names for each structure. The XDR source consists of data definitions, each starting with the keyword "struct" followed by the name of the structure and a pair of curly braces containing the fields of the structure. Each field is defined with a type and a name, separated by a space. The type can be "int", "string", or "bool".
"""

import re

def parseXDR(xdr_source):
    structure_fields = {}
    struct_pattern = re.compile(r'struct\s+(\w+)\s*{([^}]*)}')
    field_pattern = re.compile(r'(\w+)\s+(\w+)')

    matches = struct_pattern.findall(xdr_source)
    for match in matches:
        structure_name = match[0]
        field_list = field_pattern.findall(match[1])
        field_names = [field[1] for field in field_list]
        structure_fields[structure_name] = field_names

    return structure_fields