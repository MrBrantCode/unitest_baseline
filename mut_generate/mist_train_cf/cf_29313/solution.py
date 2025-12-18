"""
QUESTION:
Implement a function `find_fields_to_split` that takes a data structure description string and a direction integer as input, and returns a list of field names that need to be split up in the given direction. The direction 1 corresponds to splitting up fields horizontally and direction 2 corresponds to splitting up fields vertically. The data structure description is well-formatted and follows a consistent pattern, with each line representing a field in the format "field_name: data_type".
"""

from typing import List

def find_fields_to_split(datastc: str, direction: int) -> List[str]:
    fields_to_split = []
    lines = datastc.strip().split('\n')
    for line in lines:
        field, _ = line.strip().split(':')
        if direction == 1 and 'list' in line:
            fields_to_split.append(field.strip())
        elif direction == 2 and 'list' not in line:
            fields_to_split.append(field.strip())
    return fields_to_split