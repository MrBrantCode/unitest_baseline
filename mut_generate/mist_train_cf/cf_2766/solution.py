"""
QUESTION:
Create a function `longest_common_substring(str1, str2)` that takes two strings as input and returns their longest common substring. The function should have a time complexity of O(n*m), where n and m are the lengths of the input strings. The space complexity should be O(min(n,m)). The function should handle inputs containing special characters and whitespace, ignore any leading or trailing whitespace, and work correctly with non-standard character encoding formats.
"""

def longest_common_substring(str1, str2):
    str1 = str1.strip()
    str2 = str2.strip()
    
    len1 = len(str1)
    len2 = len(str2)
    
    matrix = [[0] * (len2 + 1) for _ in range(len1 + 1)]
    
    longest_length = 0
    end_position = 0
    
    for i in range(1, len1 + 1):
        for j in range(1, len2 + 1):
            if str1[i - 1] == str2[j - 1]:
                matrix[i][j] = matrix[i - 1][j - 1] + 1
                
                if matrix[i][j] > longest_length:
                    longest_length = matrix[i][j]
                    end_position = i
                    
    return str1[end_position - longest_length:end_position]