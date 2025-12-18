"""
QUESTION:
Implement a function `extract_event_info(event)` that takes a game event tuple as input and returns a dictionary containing the extracted information based on the provided pattern. The game event tuple contains an event ID, event name, lexicon group, description, parameters, and a pattern. The function should extract specific information from the parameters based on the pattern, which consists of variable placeholders prefixed with a '+' sign, followed by the variable name and an optional type indicator ('N' for string or 'G' for integer). The function should return a dictionary with the extracted information, where the keys are the variable names and the values are the corresponding extracted values. 

The input event tuple is of the format: (Event ID, Event Name, Lexicon Group, Description, Parameters, Pattern). The Parameters is a list of variables and the Pattern is a string representing the pattern to extract information.
"""

from typing import Tuple, Dict, Union

def extract_event_info(event: Tuple) -> Dict[str, Union[str, int]]:
    event_id, event_name, _, _, parameters, pattern = event
    extracted_info = {}

    for param, pattern_part in zip(parameters, pattern.split('+')[1:]):
        variable, type_indicator = pattern_part.split('#')
        if type_indicator == 'N':
            extracted_info[variable] = param
        elif type_indicator == 'G':
            extracted_info[variable] = int(param)

    return extracted_info