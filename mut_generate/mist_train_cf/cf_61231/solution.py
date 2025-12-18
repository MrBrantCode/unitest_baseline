"""
QUESTION:
Develop a function `check_string_order` that takes two number strings (`string1` and `string2`) and an operation string (`operation`) as parameters. The function checks the order of digits in `string2` within `string1` based on the specified operation, which can be 'same-order', 'reverse-order', or 'any-order'. The function should return a boolean indicating whether the condition is met. The operation string should be one of the specified values; otherwise, an error message should be printed and the function should return None.
"""

def check_string_order(string1, string2, operation):
    """
    Checks the order of digits in `string2` within `string1` based on the specified operation.
    
    Args:
    string1 (str): The string to check against.
    string2 (str): The string containing the digits to check for.
    operation (str): The order operation, which can be 'same-order', 'reverse-order', or 'any-order'.
    
    Returns:
    bool: True if the condition is met, False otherwise. None if the operation is invalid.
    """

    if operation == 'same-order':
        ptr = 0
        for char in string1:
            if char == string2[ptr]:
                ptr += 1
                if ptr == len(string2):
                    return True
        return False
 
    elif operation == 'reverse-order':
        return check_string_order(string1, string2[::-1], 'same-order')

    elif operation == 'any-order':
        for char in string2:
            if char not in string1:
                return False
        return True

    else:
        print(f'Invalid operation: {operation}')
        return None