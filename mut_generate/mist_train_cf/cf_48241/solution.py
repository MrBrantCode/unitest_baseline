"""
QUESTION:
Write a Python function `decimal_to_binary(lst)` that takes a list of integers as input and returns a list of their binary representations as lists of integers in order of significance (0th index shows least significant bit). If the input list contains a non-integer element, the function should return a precise error message.
"""

def decimal_to_binary(lst):
    """
    A function that converts a list of integers in decimal notation to
    their respective binary representations.
    :param lst: list of integers in decimal notation
    :return: list of binary equivalents for each decimal number
    """
    res_lst = []
    for i in lst:
        if not isinstance(i, int):
            return "Error: Non-integer element found"
        binary = []
        while i > 0:
            binary.append(i % 2)
            i = i // 2
        # the binary representation is stored in reversed order
        # to match the requirement of least significant bit at 0th index
        res_lst.append(binary[::-1])
    return res_lst