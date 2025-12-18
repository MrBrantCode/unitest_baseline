"""
QUESTION:
Write a function named `modify_array` that takes an array `arr` and a constant value `constant` as input. Multiply each element in the array by the constant value. If the constant value is 0, set each element in the array to 0. If the constant value is negative, reverse the order of the array elements after modification. Return the modified array.
"""

def modify_array(arr, constant):
    """
    Modify an array by multiplying each element with a constant value.
    If the constant is 0, set all elements to 0. If the constant is negative,
    reverse the array after modification.

    Args:
        arr (list): The input array.
        constant (int): The constant value.

    Returns:
        list: The modified array.
    """
    if constant == 0:
        return [0] * len(arr)
    else:
        modified_arr = [num * constant for num in arr]
        return modified_arr[::-1] if constant < 0 else modified_arr