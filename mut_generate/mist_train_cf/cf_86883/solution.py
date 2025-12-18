"""
QUESTION:
Write a function named `compare_strings` that takes two string arguments and returns -1 if the first string is lexicographically smaller, 1 if the first string is lexicographically greater, and 0 if the strings are equal. The function should ignore non-alphabet characters and consider them as less than any alphabet character, and it should handle strings with leading or trailing whitespace characters. The comparison should be case-insensitive. The function should not use any built-in string comparison functions or additional data structures. It should have a time complexity of O(n), where n is the length of the longer string.
"""

def compare_strings(s1, s2):
    # Convert strings to lowercase and remove leading/trailing whitespace
    s1 = s1.lower().strip()
    s2 = s2.lower().strip()

    # Get the lengths of the strings
    len1 = len(s1)
    len2 = len(s2)

    # Initialize variables for comparison
    i = 0
    j = 0

    # Loop through the strings until a difference is found or one of the strings ends
    while i < len1 and j < len2:
        # Check if the characters are alphabets
        if s1[i].isalpha() and s2[j].isalpha():
            # Compare the characters
            if s1[i] < s2[j]:
                return -1
            elif s1[i] > s2[j]:
                return 1
            else:
                # Move to the next characters
                i += 1
                j += 1
        else:
            # Skip non-alphabet characters
            if not s1[i].isalpha():
                i += 1
            if not s2[j].isalpha():
                j += 1

    # Handle the case where one string is a prefix of the other
    if i == len1 and j < len2:
        return -1
    elif i < len1 and j == len2:
        return 1

    # Strings are equal
    return 0