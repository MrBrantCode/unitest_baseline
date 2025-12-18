"""
QUESTION:
Write a function named `count_occurrences` that takes two parameters: a number and a nested list. The function should return the count of occurrences of the number in the nested list, excluding occurrences within sublists. The number can be a float, and if it is not a valid float, the function should return an error message.
"""

def count_occurrences(number, nested_list):
    count = 0

    # Check if the number is a valid float
    try:
        float(number)
    except ValueError:
        return "Error: Invalid float number"

    # Helper function to recursively count occurrences
    def count_recursive(lst):
        nonlocal count
        for item in lst:
            if isinstance(item, list):
                count_recursive(item)
            elif item == float(number):
                count += 1

    # Call the helper function to count occurrences
    count_recursive(nested_list)

    return count