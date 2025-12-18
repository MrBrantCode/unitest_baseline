"""
QUESTION:
Write a function named `longest_common_substring` that takes two strings `str1` and `str2` as input and returns their longest common substring. The function should not assume any specific length or content of the input strings. The function should return the longest common substring, not its length.
"""

def longest_common_substring(str1, str2):
    m = len(str1)
    n = len(str2)
    
    # An (m+1) times (n+1) matrix
    result = [[0]*(n+1) for i in range(m+1)]
    
    longest_common_sub = 0
    end_of_longest_common_sub = 0
    
    for i in range(m+1):
        for j in range(n+1):
            if i == 0 or j == 0:
                result[i][j] = 0
            elif str1[i-1] == str2[j-1]:
                result[i][j] = result[i-1][j-1] + 1
                if result[i][j] > longest_common_sub:
                    longest_common_sub = result[i][j]
                    end_of_longest_common_sub = i-1
            else:
                result[i][j] = 0

    # return the longest common substring
    return str1[end_of_longest_common_sub - longest_common_sub + 1:end_of_longest_common_sub+1]