"""
QUESTION:
Implement the `parseCommandLineOptions` function, which takes a list of command-line arguments and returns a dictionary of options and their descriptions. The options are in the format `<option> (description)`, where `<option>` starts with a hyphen and `(description)` is the corresponding description. The function should exclude the hyphen from the option keys in the output dictionary.

The input list contains command-line arguments where each option is followed by its description. The function should iterate through the list, identify the options, and pair them with their descriptions. If an option is not followed by a description, its value in the output dictionary should be an empty string.

Restrictions: The function should handle cases where an option is not followed by a description and where the input list contains non-option arguments. The output dictionary should only include options as keys.
"""

from typing import List, Dict

def parseCommandLineOptions(args: List[str]) -> Dict[str, str]:
    options = {}
    i = 0
    while i < len(args):
        if args[i].startswith('-'):
            option = args[i][1:]
            if i + 1 < len(args) and not args[i + 1].startswith('-'):
                description = args[i + 1]
                options[option] = description
                i += 1
            else:
                options[option] = ''
        i += 1
    return options