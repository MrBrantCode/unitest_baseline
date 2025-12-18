"""
QUESTION:
Create a function `convert_to_integers(input_list)` that takes a list of mixed data types (integers and strings) as input. The function should convert all integer strings to integers, remove duplicates, sort the list in ascending order, and return the sum of all integers. If the input list is empty, display an error message. The function should handle cases where the input list contains non-integer strings, which should be skipped. The time complexity of the function should be O(n), where n is the length of the input list.
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

    converted_list = list(set(converted_list))
    converted_list.sort()

    total_sum = sum(converted_list)

    return total_sum