"""
QUESTION:
Write a function `longest_common_string(string1, string2)` that finds the longest common substring between two input strings. The function should take two strings as input and return the longest common substring. If no common substring exists, the function should return an empty string.
"""

def longest_common_string(string1, string2):
    if string1 == "" or string2 == "":
        return ""
    elif string1 == string2:
        return string1
    else:
        matrix = [[0 for x in range(len(string2))] for y in range(len(string1))]
        longest_length = 0
        longest_string = ""
        for i in range(len(string1)):
            for j in range(len(string2)):
                if string1[i] == string2[j]:
                    if i == 0 or j == 0:
                        matrix[i][j] = 1
                    else:
                        matrix[i][j] = matrix[i-1][j-1] + 1
                    if matrix[i][j] > longest_length:
                        longest_length = matrix[i][j]
                        longest_string = string1[i-longest_length+1:i+1]
                else:
                    matrix[i][j] = 0
        return longest_string