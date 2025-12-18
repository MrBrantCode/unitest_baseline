"""
QUESTION:
Write a function `convert_to_integers` that takes a list of strings and/or integers as input. The function should convert all strings that can be converted to integers to integers, remove any duplicates, sort the list in ascending order, and return the list along with the sum of its elements. If the input list is empty, it should print an error message instead. The function should have a time complexity of O(n), where n is the length of the input list.
"""

def convert_to_integers(input_list):
    if len(input_list) == 0:
        print("Error: Input list is empty")
        return

    converted_list = []
    for item in input_list:
        if isinstance(item, int):
            converted_list.append(item)
        elif isinstance(item, str):
            try:
                converted_list.append(int(item))
            except ValueError:
                pass

    converted_list = sorted(list(set(converted_list)))
    total_sum = sum(converted_list)
    return converted_list, total_sum