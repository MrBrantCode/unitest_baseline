"""
QUESTION:
Extract the value associated with the key "second" from the given dictionary. The dictionary contains information about individuals with keys "first", "second", and "third", each mapping to another dictionary containing "name", "age", and "city" details. 

Write a function named `extract_second_element` that takes this dictionary as input and returns the value associated with the key "second".
"""

def extract_second_element(data):
    return data["second"]