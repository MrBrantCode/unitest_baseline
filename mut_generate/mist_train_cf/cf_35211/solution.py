"""
QUESTION:
Implement a function `count_interaction_data_options` that takes a list of options as input, where options can be one of the following types: `_ApplicationCommandInteractionDataOptionString`, `_ApplicationCommandInteractionDataOptionInteger`, `_ApplicationCommandInteractionDataOptionSubcommand`, and `_ApplicationCommandInteractionDataOptionBoolean`. The function should return a dictionary containing the count of each type of option in the input list. The dictionary keys should be the type names ("String", "Integer", "Subcommand", "Boolean") and the values should be the corresponding counts.
"""

from typing import List, Dict, Union

class _ApplicationCommandInteractionDataOptionString:
    pass

class _ApplicationCommandInteractionDataOptionInteger:
    pass

class _ApplicationCommandInteractionDataOptionSubcommand:
    pass

class _ApplicationCommandInteractionDataOptionBoolean:
    pass

def count_interaction_data_options(options: List[Union[_ApplicationCommandInteractionDataOptionString, _ApplicationCommandInteractionDataOptionInteger, _ApplicationCommandInteractionDataOptionSubcommand, _ApplicationCommandInteractionDataOptionBoolean]]) -> Dict[str, int]:
    count_dict = {
        "String": 0,
        "Integer": 0,
        "Subcommand": 0,
        "Boolean": 0
    }
    
    for option in options:
        if isinstance(option, _ApplicationCommandInteractionDataOptionString):
            count_dict["String"] += 1
        elif isinstance(option, _ApplicationCommandInteractionDataOptionInteger):
            count_dict["Integer"] += 1
        elif isinstance(option, _ApplicationCommandInteractionDataOptionSubcommand):
            count_dict["Subcommand"] += 1
        elif isinstance(option, _ApplicationCommandInteractionDataOptionBoolean):
            count_dict["Boolean"] += 1
    
    return count_dict