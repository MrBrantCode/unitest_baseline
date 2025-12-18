"""
QUESTION:
Develop a function called `longestCommonPrefix` that takes two strings `str1` and `str2` as input and returns the longest common prefix between them. The function should compare characters at corresponding positions in both strings and return the common prefix as soon as it encounters a mismatch.
"""

def longestCommonPrefix(str1, str2): 
    """
    Returns the longest common prefix between two input strings.

    Args:
    str1 (str): The first input string.
    str2 (str): The second input string.

    Returns:
    str: The longest common prefix between str1 and str2.
    """
    n1 = len(str1) 
    n2 = len(str2) 
  
    result = "" 
    j = 0
    i = 0
    while(i <= n1 - 1 and j <= n2 - 1): 
        if (str1[i] != str2[j]): 
            break
        result += str1[i] 
        i += 1
        j += 1
  
    return result