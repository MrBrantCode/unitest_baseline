"""
QUESTION:
Create a function `longest_common_substring` that takes two input strings and returns the longest common substring. The function should be able to handle cases where the input strings contain special characters and have a time complexity of O(n^2), where n is the length of the longest input string.
"""

def longest_common_substring(str1, str2):
    # Create a table to store the lengths of common substrings
    table = [[0] * (len(str2) + 1) for _ in range(len(str1) + 1)]
    
    # Variables to store the maximum length and ending position of the longest common substring
    max_length = 0
    end_pos = 0
    
    # Fill the table and update max_length and end_pos as we go
    for i in range(1, len(str1) + 1):
        for j in range(1, len(str2) + 1):
            if str1[i - 1] == str2[j - 1]:
                table[i][j] = table[i - 1][j - 1] + 1
                if table[i][j] > max_length:
                    max_length = table[i][j]
                    end_pos = i
    
    # Extract the longest common substring using end_pos and max_length
    longest_substring = str1[end_pos - max_length: end_pos]
    
    return longest_substring