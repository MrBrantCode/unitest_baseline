"""
QUESTION:
Implement a function named `get_default_value` that retrieves the default value for a given section and option from a configuration file in INI format. The function should take three parameters: `config_file` (the path to the configuration file), `section` (the name of the section), and `option` (the name of the option). It should return the retrieved value in its correct data type (string, integer, float, boolean, or None if the section or option does not exist). The function should attempt to convert the value to an integer if it is a string representation of an integer, to a float if it is a string representation of a floating-point number, and to a boolean if it is a string representation of a boolean. If the value cannot be converted to any of these types, it should be returned as a string.
"""

from configparser import ConfigParser
from typing import Union

def get_default_value(config_file: str, section: str, option: str) -> Union[str, int, float, bool, None]:
    parser = ConfigParser()
    parser.read(config_file)
    
    if section in parser:
        if option in parser[section]:
            value = parser[section][option]
            if value.isdigit():
                return int(value)
            elif value.replace('.', '', 1).isdigit():
                return float(value)
            elif value.lower() == 'true' or value.lower() == 'false':
                return value.lower() == 'true'
            else:
                return value
    return None