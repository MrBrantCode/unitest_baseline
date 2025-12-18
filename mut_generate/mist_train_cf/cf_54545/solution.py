"""
QUESTION:
Construct a function `ini_to_json` that takes the path to an INI configuration file as input, parses the file, determines the data type of each value (integer, boolean, or string), and returns a JSON representation of the configuration. The function should handle boolean values represented as 'true' or 'false' (case-insensitive) and integer values. The JSON representation should be in a nested dictionary format, where each section of the INI file is a key in the outer dictionary, and each key-value pair in the section is a key-value pair in the inner dictionary.
"""

import json
import configparser

def ini_to_json(ini_file):
    config = configparser.ConfigParser()
    config.read(ini_file)

    # Initialize a json dictionary
    json_dict = {}

    # Iterate over the sections in the INI file
    for section in config.sections():
        # Initialize section's dictionary
        json_dict[section] = {}

        # Iterate over key, value pairs in the section
        for key, val in config.items(section):
            # try to parse value as int
            try:
                val = int(val)
            except ValueError:
                # try to parse value as bool
                if val.lower() in ['true', 'false']:
                    val = val.lower() == 'true'
            # add key, value pair to section's dictionary
            json_dict[section][key] = val

    return json.dumps(json_dict, indent=4)