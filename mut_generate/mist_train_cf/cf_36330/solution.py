"""
QUESTION:
Write a function `extract_keywords(config_data)` that takes a nested configuration data structure as input, where each tuple represents a key-value pair and each dictionary represents a section with its own key-value pairs. The keys and values can be strings, lists, or nested dictionaries. The function should return a dictionary containing all the keywords and their corresponding values.
"""

def extract_keywords(config_data):
    result = {}

    def extract(data):
        if isinstance(data, tuple):
            result[data[0]] = data[1]
        elif isinstance(data, dict):
            for key, value in data.items():
                if isinstance(value, (str, list)):
                    result[key] = value
                else:
                    extract(value)

    for item in config_data:
        if isinstance(item, (tuple, dict)):
            extract(item)

    return result