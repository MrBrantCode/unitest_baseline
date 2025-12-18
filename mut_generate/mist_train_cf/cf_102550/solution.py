"""
QUESTION:
Compare two given strings to determine their equality. If the strings are not equal, return the index position at which they differ. Consider strings of different lengths as unequal, and perform the comparison in a case-sensitive manner.
"""

def compare_strings(str1, str2):
    """
    Compare two given strings to determine their equality.
    If the strings are not equal, return the index position at which they differ.
    
    Parameters:
    str1 (str): The first string to compare.
    str2 (str): The second string to compare.
    
    Returns:
    int: The index position at which the strings differ if they are not equal.
         -1 if the strings are equal.
    """
    for i in range(min(len(str1), len(str2))):
        if str1[i] != str2[i]:
            return i
    if len(str1) != len(str2):
        return min(len(str1), len(str2))
    return -1