"""
QUESTION:
Implement the function `generate_config_string(config: dict) -> str` where `config` is a dictionary containing configuration settings with keys as setting names and values as dictionaries with keys `default` and `show_default`. The function should return a string representing the formatted configuration settings, following these rules:
- If a setting has a `default` value and `show_default` is `True`, include `key=default_value` in the string.
- Otherwise, include only `key=value` in the string if a value exists; otherwise, include just the key.
"""

def generate_config_string(config: dict) -> str:
    formatted_settings = []
    for key, value in config.items():
        if "default" in value and value["show_default"]:
            formatted_settings.append(f"{key}={value['default']}")
        else:
            formatted_settings.append(key)
    return ",".join(formatted_settings)