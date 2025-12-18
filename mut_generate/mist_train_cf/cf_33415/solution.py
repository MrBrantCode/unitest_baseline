"""
QUESTION:
Implement a function `matchNames(ID_name, ID, data)` that takes in a string `ID_name`, a value `ID` which can be either a string or an integer, and a list of dictionaries `data`. The function should return a list of IDs from the dictionaries in `data` where the value of the key `ID_name` matches the given `ID`.
"""

def matchNames(ID_name, ID, data):
    matched_ids = []
    for item in data:
        if item.get(ID_name) == ID:
            matched_ids.append(item.get('ID'))
    return matched_ids