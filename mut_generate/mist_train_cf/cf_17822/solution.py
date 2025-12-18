"""
QUESTION:
Create a function named `identify_type` that takes a list of mixed data types as input. The function should return a list of strings representing the type of each element in the input list. The types should be classified as "alphabet" for single alphabetic characters (A-Z or a-z), "number" for integers, and "special character" for all other elements. The output list should maintain the same order as the input list.
"""

def identify_type(data):
    types = []
    for element in data:
        if isinstance(element, str) and len(element) == 1 and element.isalpha():
            types.append("alphabet")
        elif isinstance(element, int):
            types.append("number")
        else:
            types.append("special character")
    return types