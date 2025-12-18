"""
QUESTION:
Implement a function `save_information_str` that takes a dictionary `note_dict` as input and returns a string containing its key-value pairs in the format "[key1]value1|[key2]value2|...". The function should iterate through the dictionary, append each key-value pair to a string, and return the formatted string. The function should handle any number of key-value pairs and exclude the extra "|" at the end of the string.
"""

def save_information_str(note_dict: dict) -> str:
    strr = ""
    for key, value in note_dict.items():
        strr = strr + "[{0}]{1}|".format(key, value)
    return strr[:-1]  # Remove the extra '|' at the end