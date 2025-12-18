"""
QUESTION:
Write a Python function `flatten_and_sum(input_list)` that calculates the sum of unique numeric elements and the count of these elements within a provided list. The list may contain nested lists, dictionaries, and sets of up to 5 levels deep. The function should convert non-numeric elements to numerical values where possible and ignore non-numeric elements and None values. The function should not use built-in Python functions for flattening the list or calculating the sum, and should handle exceptions and errors gracefully. The function should be optimized for time complexity to handle large lists.
"""

def flatten_and_sum(input_list):
    total_sum = 0
    num_unique = 0
    unique_elements = set()

    def recursive_flatten(item):
        nonlocal total_sum, num_unique
        if isinstance(item, list):
            for element in item:
                recursive_flatten(element)
        elif isinstance(item, dict):
            for value in item.values():
                recursive_flatten(value)
        elif isinstance(item, set):
            for element in item:
                recursive_flatten(element)
        else:
            # Try to convert item to float
            try:
                numeric = float(item)
                if numeric not in unique_elements:
                    unique_elements.add(numeric)
                    total_sum += numeric
                    num_unique += 1
            except (TypeError, ValueError):
                pass

    recursive_flatten(input_list)

    return total_sum, num_unique