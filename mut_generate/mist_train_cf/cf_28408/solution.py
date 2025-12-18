"""
QUESTION:
Create a function `format_network_config(config: dict) -> str` that takes a dictionary `config` as input, where each key-value pair represents a network management configuration parameter, and returns a formatted string representing the configuration. The function should format the parameters in the following format: `Parameter1: Value1 Parameter2: Value2 ...`. It should also obfuscate any sensitive information, such as passwords, by replacing the actual value with asterisks (*) of the same length.
"""

def format_network_config(config: dict) -> str:
    formatted_config = ""
    for key, value in config.items():
        if 'password' in key.lower():
            formatted_value = '*' * len(value)
        else:
            formatted_value = value
        formatted_config += f"{key}: {formatted_value}\n"
    return formatted_config.strip()