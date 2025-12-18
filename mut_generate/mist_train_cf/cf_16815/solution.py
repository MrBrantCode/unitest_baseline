"""
QUESTION:
Create a function `list_to_dict` that takes a list of alternating numbers and letters as input and returns a dictionary where the keys are the numbers and the values are the corresponding letters. If a number appears multiple times in the list, the corresponding value in the dictionary should be a list of letters.
"""

def list_to_dict(lst):
    result = {}
    for i in range(0, len(lst), 2):
        key = lst[i]
        value = lst[i+1]
        if key in result:
            if isinstance(result[key], list):
                result[key].append(value)
            else:
                result[key] = [result[key], value]
        else:
            result[key] = value
    return result