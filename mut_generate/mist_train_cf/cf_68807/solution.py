"""
QUESTION:
Write a function `find_words` that takes an iterable and an integer `length` as input and returns a list of all string elements in the iterable with a length equal to the input length. The function should validate that all elements of the iterable are strings and print the index of the first non-string element encountered. If the input is a string, the function should print an error message and return an empty list. The function should be able to handle any type of iterable and be optimized for large data inputs.
"""

def find_words(iterable, length):
    result = []
    if isinstance(iterable, str):
        print("The input is a string. Please input an iterable.")
        return []
    for i, element in enumerate(iterable):
        if not isinstance(element, str):
            print(f'The element at index {i} is not a string.')
            continue
        if len(element) == length:
            result.append(element)
    return result