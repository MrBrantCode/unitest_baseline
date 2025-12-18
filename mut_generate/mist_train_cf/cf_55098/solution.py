"""
QUESTION:
Create a function `perform_operation_and_calculate_mean` that takes two lists of numbers `arr1` and `arr2` and an operation as input. The operation can be one of the four basic arithmetic operations: addition, subtraction, multiplication, or division. The function should perform the operation element-wise on the two input lists, calculate the mean of the resulting list, and return the result. 

The function should be able to handle the following cases:

- The input lists have the same length.
- The operation is one of the four basic arithmetic operations (case-insensitive).
- The input lists contain only numbers.
- Division by zero does not occur.

If any of these conditions are not met, the function should return an error message. The operation can be specified using either a symbol (e.g., "+", "-", "*", "/") or a word (e.g., "add", "subtract", "multiply", "divide").
"""

def perform_operation_and_calculate_mean(arr1, arr2, operation):
    """
    This function performs an element-wise operation on two input lists, calculates the mean of the resulting list, and returns the result.

    Args:
        arr1 (list): The first list of numbers.
        arr2 (list): The second list of numbers.
        operation (str): The operation to be performed. It can be one of the four basic arithmetic operations (case-insensitive).

    Returns:
        float: The mean of the resulting list after performing the operation.
    """

    # Check if the input lists have the same length
    if len(arr1) != len(arr2):
        return "Array lengths are not equal!"

    # Perform the operation element-wise on the two input lists
    try:
        if operation.lower() in ["+", "add"]:
            resulting_array = [a+b for a,b in zip(arr1, arr2)]
        elif operation.lower() in ["-", "subtract"]:
            resulting_array = [a-b for a,b in zip(arr1, arr2)]
        elif operation.lower() in ["*", "multiply"]:
            resulting_array = [a*b for a,b in zip(arr1, arr2)]
        elif operation.lower() in ["/", "divide"]:
            resulting_array = [a/b for a,b in zip(arr1, arr2)]
        else:
            return "Please enter a valid operation!"
    except TypeError:
        return "Array elements should be numbers!"
    except ZeroDivisionError:
        return "Cannot divide by zero!"

    # Calculate the mean of the resulting list
    try:
        mean = sum(resulting_array)/len(resulting_array)
    except TypeError:
        return "Array elements should be numbers!"

    return mean