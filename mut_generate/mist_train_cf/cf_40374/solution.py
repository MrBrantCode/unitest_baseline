"""
QUESTION:
Write a function `parse_entity_codes(input_string: str) -> dict` that takes a string `input_string` as input and returns a dictionary where the keys are the entity codes and the values are the corresponding descriptions. Each entity code is in the format of a number followed by a hyphen, and the descriptions are the text following the hyphen until the next entity code. The input string is a multi-line string with each entity code and description on a separate line. The entity code in the output dictionary should be an integer if it is a single number, otherwise it should be a string.
"""

def parse_entity_codes(input_string: str) -> dict:
    entity_dict = {}
    lines = input_string.strip().split('\n')
    for line in lines:
        code, description = line.split(' - ', 1)
        entity_dict[code if code.isdigit() == False else int(code)] = description.strip()
    return entity_dict