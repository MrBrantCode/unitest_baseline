"""
QUESTION:
Implement a function `equal_lengths` to check if two input strings have equal lengths, and another function `count_similar_chars` to count the number of similar characters between the two strings. The strings can contain spaces and punctuation marks. Do not use any built-in or external libraries or functions that directly compare the lengths of strings or count the number of similar characters. The time complexity of the solution should be no worse than O(n), where n is the length of the longest string.
"""

def equal_lengths(string1, string2):
    """
    This function checks if the lengths of two strings are equal.
    """
    len1 = 0
    len2 = 0

    # Iterate through both strings to calculate their lengths
    for _ in string1:
        len1 += 1
    for _ in string2:
        len2 += 1

    # Return true if lengths are equal, otherwise return false
    if len1 == len2:
        return True
    else:
        return False


def count_similar_chars(string1, string2):
    """
    This function counts the number of similar characters between two strings,
    assuming the strings have the same length.
    """
    # Initialize a counter for the number of similar characters
    count = 0

    # Iterate through the two strings using a common index
    index = 0
    for char1 in string1:
        # If the characters at the current index are equal, increment the counter
        if char1 == string2[index]:
            count += 1
        index += 1

    return count