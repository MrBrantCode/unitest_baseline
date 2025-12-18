"""
QUESTION:
Implement a function `parse_config(config_text: str) -> dict` that takes a string `config_text` representing the content of a configuration file and returns a dictionary where the keys are the strings before the hyphens and the values are the descriptions or options after the hyphens. Each key-value pair in `config_text` is separated by a hyphen (-) and may span multiple lines.
"""

def entrance(config_text: str) -> dict:
    config_dict = {}
    lines = config_text.split('\n')
    key = None
    value = ""
    for line in lines:
        line = line.strip()
        if line.startswith('-'):
            if key is not None:
                config_dict[key] = value.strip()
            key = line[1:].strip()
            value = ""
        else:
            value += line + " "
    if key is not None:
        config_dict[key] = value.strip()
    return config_dict