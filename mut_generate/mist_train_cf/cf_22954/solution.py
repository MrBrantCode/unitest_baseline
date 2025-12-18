"""
QUESTION:
Write a function named `count_matches` that takes two same-length strings as input and returns the number of character matches in the same position without using any loops or built-in functions, with a time complexity of O(n), where n is the length of the strings.
"""

def count_matches(s1, s2):
    """
    This function counts the number of character matches in the same position 
    between two strings without using any loops or built-in functions, 
    with a time complexity of O(n), where n is the length of the strings.

    Parameters:
    s1 (str): The first input string.
    s2 (str): The second input string.

    Returns:
    int: The number of character matches between the two strings.
    """

    # Convert strings to ASCII codes
    ascii1 = [ord(c) for c in s1]
    ascii2 = [ord(c) for c in s2]

    # Perform bitwise operations
    xor_result = [a ^ b for a, b in zip(ascii1, ascii2)]
    not_result = [~x for x in xor_result]
    and_result = [a & b for a, b in zip(xor_result, not_result)]
    not_and_result = [~x for x in and_result]
    final_result = [a & b for a, b in zip(and_result, not_and_result)]

    # Count the number of set bits in final_result
    matches = sum(bin(x).count('1') for x in final_result)

    return matches