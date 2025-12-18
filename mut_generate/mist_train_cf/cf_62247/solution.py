"""
QUESTION:
Create a function `custom_base_arithmetic` that takes four parameters: `m`, `base`, `operation`, and `val`. The function should perform a specific arithmetic operation on a list of numbers from 0 to `m` (inclusive), then apply the modulo operation with `val`. The result should be converted to the given `base`. 

Restrictions: 
- `m` must be greater than or equal to 0
- `base` must be between 2 and 16 (inclusive)
- `val` must not be 0
- `operation` can be one of "sum", "diff", "product", "average", or "modulo" 

Return -1 for invalid inputs.
"""

def custom_base_arithmetic(m, base, operation, val):
    """
    This function performs a specific arithmetic operation on a list of numbers from 0 to `m` (inclusive), 
    then apply the modulo operation with `val`. The result is converted to the given `base`.

    Parameters:
    m (int): The upper limit of the list of numbers.
    base (int): The base to convert the result to.
    operation (str): The arithmetic operation to perform.
    val (int): The value to apply the modulo operation with.

    Returns:
    str: The result of the arithmetic operation in the given base, or -1 for invalid inputs.
    """

    # Check for invalid inputs
    if not (0 <= m) or not (2 <= base <= 16) or val == 0:
        return -1

    # Generate the list of numbers from 0 to m
    num_list = list(range(m + 1))

    # Perform the specified arithmetic operation
    if operation == "sum":
        initial_val = sum(num_list)
    elif operation == "diff":
        initial_val = num_list[0]
        for i in range(1, len(num_list)):
            initial_val -= num_list[i]
    elif operation == "product":
        initial_val = 1
        for i in num_list:
            initial_val *= i
    elif operation == "average":
        initial_val = sum(num_list) // len(num_list)
    elif operation == "modulo":
        initial_val = num_list[0]
        for i in range(1, len(num_list)):
            initial_val %= num_list[i]
    else:
        return -1

    # Apply the modulo operation
    result = round(initial_val % val)

    # Convert the result to the given base
    if base == 2:
        return bin(result)[2:]  # Remove the '0b' prefix
    elif base == 8:
        return oct(result)[2:]  # Remove the '0o' prefix
    elif base == 10:
        return str(result)
    elif base == 16:
        return hex(result)[2:]  # Remove the '0x' prefix
    else:
        return -1