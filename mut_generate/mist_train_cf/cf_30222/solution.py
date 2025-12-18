"""
QUESTION:
Write a function `process_list` that takes a list of elements as input, where elements can be strings, numbers, or lists. The function should return a new list where strings are converted to uppercase, numbers are squared, and lists have their elements reversed.
"""

def process_list(input_list):
    processed_list = []
    for element in input_list:
        if isinstance(element, str):
            processed_list.append(element.upper())
        elif isinstance(element, int) or isinstance(element, float):
            processed_list.append(element ** 2)
        elif isinstance(element, list):
            processed_list.append(list(reversed(element)))
    return processed_list