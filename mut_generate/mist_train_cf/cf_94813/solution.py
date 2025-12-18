"""
QUESTION:
Create a function named `longest_common_substring` that takes two strings `str1` and `str2` as input and returns the longest common substring between them. The function should have a time complexity of O(n*m), where n is the length of `str1` and m is the length of `str2`. The function should also have a space complexity of O(min(n,m)). The function should handle inputs containing special characters and whitespace, and it should ignore any leading or trailing whitespace in the input strings.
"""

def longest_common_substring(str1, str2):
    # Remove leading and trailing whitespace
    str1 = str1.strip()
    str2 = str2.strip()

    # Initialize a table to store the lengths of common substrings
    table = [[0] * (len(str2) + 1) for _ in range(len(str1) + 1)]

    # Variables to keep track of the longest common substring and its length
    longest_length = 0
    longest_end_index = 0

    # Fill in the table
    for i in range(1, len(str1) + 1):
        for j in range(1, len(str2) + 1):
            if str1[i - 1] == str2[j - 1]:
                table[i][j] = table[i - 1][j - 1] + 1
                if table[i][j] > longest_length:
                    longest_length = table[i][j]
                    longest_end_index = i

    # Extract the longest common substring
    longest_substring = str1[longest_end_index - longest_length: longest_end_index]

    return longest_substring