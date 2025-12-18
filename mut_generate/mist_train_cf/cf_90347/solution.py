"""
QUESTION:
Create a function `multiply_lists(list1, list2)` that takes two lists as input and returns a new list where each element is the product of the corresponding elements in the input lists. The input lists should have the same length and can contain positive or negative integers, or strings representing integers. If the input lists are empty or have different lengths, the function should return an error message. The function should also handle cases where the input lists contain nested lists, floating-point numbers, or non-integer strings, and return an error message in these cases.
"""

def multiply_lists(list1, list2):
    # Check if input lists are empty or have different lengths
    if len(list1) == 0 or len(list2) == 0:
        return "Error: Input lists cannot be empty."
    if len(list1) != len(list2):
        return "Error: Input lists must have the same length."

    result = []
    for i in range(len(list1)):
        # Check if elements are nested lists
        if isinstance(list1[i], list) and isinstance(list2[i], list):
            nested_result = multiply_lists(list1[i], list2[i])
            result.append(nested_result)
        # Check if elements are strings
        elif isinstance(list1[i], str) and isinstance(list2[i], str):
            try:
                num1 = int(list1[i])
                num2 = int(list2[i])
                result.append(num1 * num2)
            except ValueError:
                return "Error: Input lists contain non-integer strings."
        # Check if elements are floating-point numbers
        elif isinstance(list1[i], float) or isinstance(list2[i], float):
            return "Error: Input lists contain floating-point numbers."
        # Check if elements are non-positive integers
        elif not isinstance(list1[i], int) or not isinstance(list2[i], int) or list1[i] <= 0 or list2[i] <= 0:
            return "Error: Input lists contain non-positive integers."
        # Multiply corresponding positive or negative integers
        else:
            result.append(list1[i] * list2[i])

    return result