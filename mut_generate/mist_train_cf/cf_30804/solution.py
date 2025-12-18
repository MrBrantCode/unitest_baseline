"""
QUESTION:
Implement the function `parse_config(config_dict, input_dict)` that takes two dictionaries as input:
- `config_dict`: a dictionary where each key represents a configuration parameter and its corresponding value is another dictionary containing the parameter's type and default value.
- `input_dict`: a dictionary containing the configuration values to be parsed.

Return a new dictionary with the parsed values, ensuring they adhere to their specified types in `config_dict`. If a key is missing in `input_dict`, use the default value from `config_dict`.

Restrictions:
- Supported types are `int`, `str`, and `bool`.
- For `bool`, "True" and "true" are considered as `True` and any other value is considered as `False`.
"""

def parse_config(config_dict, input_dict):
    parsed_dict = {}
    for key, value in config_dict.items():
        if key in input_dict:
            if value["type"] == int:
                parsed_dict[key] = int(input_dict[key])
            elif value["type"] == str:
                parsed_dict[key] = str(input_dict[key])
            elif value["type"] == bool:
                parsed_dict[key] = input_dict[key].lower() == "true"
            else:
                parsed_dict[key] = input_dict[key]
        else:
            parsed_dict[key] = value["default"]
    return parsed_dict