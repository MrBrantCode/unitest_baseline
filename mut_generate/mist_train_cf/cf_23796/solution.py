"""
QUESTION:
Write a function `longest_common_subsequence_length` to find the length of the longest common subsequence of two given strings. The function should take two strings as input and return an integer representing the length of their longest common subsequence.
"""

def longest_common_subsequence_length(str1, str2):
    """
    This function calculates the length of the longest common subsequence of two given strings.
    
    Parameters:
    str1 (str): The first input string.
    str2 (str): The second input string.
    
    Returns:
    int: The length of the longest common subsequence.
    """
    arr = [[0] * (len(str2) + 1) for _ in range(len(str1) + 1)]
    max_length = 0
    
    for i in range(1, len(str1) + 1):
        for j in range(1, len(str2) + 1):
            if str1[i - 1] == str2[j - 1]:
                arr[i][j] = arr[i - 1][j - 1] + 1
                max_length = max(arr[i][j], max_length)
            else:
                arr[i][j] = max(arr[i][j - 1], arr[i - 1][j])
    
    return max_length