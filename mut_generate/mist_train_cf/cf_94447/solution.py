"""
QUESTION:
Implement a function `delete_occurrences(str1, str2)` that takes two strings `str1` and `str2` as input, deletes all occurrences of `str2` from `str1`, and returns the modified string. The solution should have a time complexity of O(n), where n is the length of `str1`, and a space complexity of O(1). The function should handle edge cases efficiently and should not use any built-in string manipulation functions or regular expressions, recursion, or additional data structures to store intermediate results.
"""

def delete_occurrences(str1, str2):
    # Calculate the lengths of the strings
    len1 = len(str1)
    len2 = len(str2)

    # Handle edge cases
    if len2 == 0:
        return str1

    # Initialize pointers for the first and second strings
    i = 0
    j = 0

    # Iterate through the first string
    while i < len1:
        # If the characters match, move the pointers
        if str1[i] == str2[j]:
            i += 1
            j += 1

            # If we have matched the entire second string,
            # remove it from the first string
            if j == len2:
                str1 = str1[:i-len2] + str1[i:]
                len1 -= len2
                i -= len2
                j = 0
        else:
            # If the characters don't match, reset the second pointer
            j = 0
            i += 1

    return str1