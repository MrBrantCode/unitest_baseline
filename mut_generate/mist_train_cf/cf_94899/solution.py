"""
QUESTION:
Create a function `identify_type` that takes a list of elements as input, where each element can be a combination of alphabets, numbers, and special characters. The function should return a list of the types of elements in the same order as the original data, where the type of each element is classified as "alphabet", "number", or "special character" based on the following definitions:

- Alphabets: single characters from A-Z or a-z
- Numbers: integers
- Special characters: any element that is not an alphabet or a number
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