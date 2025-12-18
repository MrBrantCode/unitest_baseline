"""
QUESTION:
Write a function named `calculate_sum` that takes a list of elements as input. The input list can be nested and contains a mix of numeric and non-numeric elements. The function should calculate the sum of all numeric elements in the list, ignoring non-numeric elements. The function must implement its own logic to calculate the sum without using any built-in sum functions.
"""

def calculate_sum(lst):
    def flatten(nested_list):
        flat_list = []
        for item in nested_list:
            if isinstance(item, list):
                flat_list.extend(flatten(item))
            else:
                flat_list.append(item)
        return flat_list

    total_sum = 0
    flat_list = flatten(lst)
    for element in flat_list:
        if isinstance(element, (int, float)):
            total_sum += element
    return total_sum