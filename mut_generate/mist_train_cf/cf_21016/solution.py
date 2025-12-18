"""
QUESTION:
Write a function `add_numbers(list1, list2)` that adds two numbers represented as lists of integers, where each integer is in the range of 0 to 9. The function should return the result as a new list, handling carry-over digits to the next position when the sum exceeds 9. If the lengths of `list1` and `list2` are not equal, raise an exception with the message "The lengths of the input lists are not equal." If any element in `list1` or `list2` is outside the range of 0 to 9, raise an exception with the message "The input lists contain values outside the valid range."
"""

def add_numbers(list1, list2):
    """
    Adds two numbers represented as lists of integers, handling carry-over digits to the next position when the sum exceeds 9.

    Args:
    list1 (list): The first list of integers.
    list2 (list): The second list of integers.

    Returns:
    list: The result as a new list.

    Raises:
    Exception: If the lengths of the input lists are not equal.
    Exception: If any element in the input lists is outside the range of 0 to 9.
    """

    if len(list1) != len(list2):
        raise Exception("The lengths of the input lists are not equal.")
    if any(x < 0 or x > 9 for x in list1 + list2):
        raise Exception("The input lists contain values outside the valid range.")

    carry = 0
    result = []
    for i in range(len(list1) - 1, -1, -1):
        sum = list1[i] + list2[i] + carry
        carry = sum // 10
        result.insert(0, sum % 10)

    if carry > 0:
        result.insert(0, carry)

    return result