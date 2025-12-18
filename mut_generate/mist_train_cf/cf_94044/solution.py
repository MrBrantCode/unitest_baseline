"""
QUESTION:
Write a function `find_max_nested` that takes a dictionary as input and returns a tuple containing the key and sum of the maximum element based on the sum of the values of its nested dictionaries, considering the sum of the values in its immediate child dictionaries. The function should have a time complexity of O(n), where n is the total number of key-value pairs in the dictionary.
"""

def find_max_nested(dictionary):
    max_sum = float('-inf')
    max_element = None

    def calculate_sum(nested_dict):
        total_sum = sum(nested_dict.values())

        for nested in nested_dict.values():
            if isinstance(nested, dict):
                total_sum += calculate_sum(nested)

        return total_sum

    for key, value in dictionary.items():
        if isinstance(value, dict):
            total_sum = calculate_sum(value)
            if total_sum > max_sum:
                max_sum = total_sum
                max_element = key

    return max_element, max_sum