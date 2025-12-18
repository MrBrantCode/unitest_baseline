"""
QUESTION:
Implement a function `longest_common_substring(str1, str2)` that finds the length of the longest common substring between two input strings `str1` and `str2` without using any built-in string functions or libraries. The function should have a time complexity of O(s1*s2) where s1 and s2 are the lengths of `str1` and `str2`, respectively.
"""

def longest_common_substring(str1, str2):
    str1_length = len(str1)
    str2_length = len(str2)

    # table to save previously calculated longest common substring
    # dimensions are string lengths + 1, initially filled with zeros
    table = [[0 for _ in range(str2_length+1)] for _ in range(str1_length+1)]
    result = 0 # to store length of longest common substring 

    for i in range(str1_length + 1):
        for j in range(str2_length + 1):
            if (i == 0 or j == 0): # initial condition, if any string is empty 
                table[i][j] = 0
            elif (str1[i-1] == str2[j-1]): # if characters match
                table[i][j] = table[i - 1][j - 1] + 1
                result = max(result, table[i][j])
            else: 
                table[i][j] = 0

    return result