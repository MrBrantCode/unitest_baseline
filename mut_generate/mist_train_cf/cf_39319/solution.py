"""
QUESTION:
Create a function `calculate_result` that takes two parameters: `operation` and `numbers`. The `operation` parameter is a string that specifies the operation to be performed on the list of numbers. The `numbers` parameter is a list of integers. 

The function should support the following operations: `sum`, `average`, `max`, and `min`. For the `sum` operation, return the sum of all the numbers in the list. For the `average` operation, return the average of all the numbers in the list. For the `max` operation, return the maximum value in the list. For the `min` operation, return the minimum value in the list.

If the operation is not one of the supported operations, the function should return an error message. Assume that the input list of numbers is valid and non-empty.
"""

def calculate_result(operation, numbers):
    """
    Perform a specified operation on a list of numbers.

    Args:
    operation (str): The operation to be performed. Supported operations are 'sum', 'average', 'max', and 'min'.
    numbers (list): A list of integers.

    Returns:
    The result of the operation if it is supported, otherwise an error message.
    """

    if operation == 'sum':
        return sum(numbers)
    elif operation == 'average':
        return sum(numbers) / len(numbers)
    elif operation == 'max':
        return max(numbers)
    elif operation == 'min':
        return min(numbers)
    else:
        return "Invalid operation. Supported operations: sum, average, max, min"