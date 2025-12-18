"""
QUESTION:
Create a function named `find_closest_elements` that takes a list of integers as input and returns a tuple of the two closest unique numbers. The input list must contain at least four unique numbers and may contain negative numbers. The function should handle edge cases, such as non-integer values and lists with less than four unique elements, but does not need to handle an empty list. If the input list contains less than four unique numbers, return an error message. If multiple pairs of numbers have the same minimum difference, any pair can be returned.
"""

def find_closest_elements(input_list):
    # Check if input_list has at least 4 unique numbers
    if len(set(input_list)) < 4:
        return 'Error: Input list should contain at least 4 unique numbers.'

    else:
        unique_list = list(set(input_list))  # Remove duplicates
        unique_list.sort()  # Sort the list
        min_diff = float('inf')  # Initialize minimum difference
        result = ()  # Initialize the result pair

        # Check all pairs of elements
        for i in range(1, len(unique_list)):
            diff = unique_list[i] - unique_list[i - 1]
            if diff < min_diff:
                min_diff = diff
                result = (unique_list[i - 1], unique_list[i])

        return result