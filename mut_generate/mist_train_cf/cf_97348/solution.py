"""
QUESTION:
Write a function `count_character_matches` that takes two strings `str1` and `str2` as input. The function should return the number of character matches between the two strings at the same position. The function must have a time complexity of O(n), where n is the length of the strings, and it should not use any loops or built-in functions (except for `ord` and `bin`). The function should assume that the input strings are of the same length.
"""

def count_character_matches(str1, str2):
    # Convert strings to ASCII codes
    ascii1 = [ord(c) for c in str1]
    ascii2 = [ord(c) for c in str2]

    # Perform bitwise operations
    xor_result = [a ^ b for a, b in zip(ascii1, ascii2)]
    not_result = [~x for x in xor_result]
    and_result = [a & b for a, b in zip(xor_result, not_result)]
    not_and_result = [~x for x in and_result]
    final_result = [a & b for a, b in zip(and_result, not_and_result)]

    # Count the number of set bits in final_result
    matches = sum(bin(x).count('1') for x in final_result)

    return matches