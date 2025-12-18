"""
QUESTION:
Write a function named `compare_strings` that takes two strings as input and returns the total number of characters that are different and their corresponding positions. The function should compare the characters at the same position in both strings. If a position exists in one string but not the other, it should also be counted as a difference. The strings may be of different lengths.
"""

def compare_strings(str1, str2):
    """
    This function compares two input strings and returns the total number of characters 
    that are different and their corresponding positions.

    Parameters:
    str1 (str): The first input string.
    str2 (str): The second input string.

    Returns:
    A tuple containing the total number of characters that are different and a list 
    of their corresponding positions.
    """
    max_len = max(len(str1), len(str2))
    diff_count = 0
    diff_positions = []

    for i in range(max_len):
        if i >= len(str1):
            diff_count += 1
            diff_positions.append(f"{i+1}.   -> {str2[i]}")
        elif i >= len(str2):
            diff_count += 1
            diff_positions.append(f"{i+1}. {str1[i]} ->   ")
        elif str1[i] != str2[i]:
            diff_count += 1
            diff_positions.append(f"{i+1}. {str1[i]} -> {str2[i]}")

    return diff_count, diff_positions