"""
QUESTION:
Write a function `longest_common_substring` that finds the longest common substring between two input strings. The function should take two strings as input and return the longest common substring. The function should have a time complexity of O(n*m), where n is the length of the first string and m is the length of the second string.
"""

def longest_common_substring(string1, string2):
    """
    Finds the longest common substring between two input strings.
    
    Args:
    string1 (str): The first input string.
    string2 (str): The second input string.
    
    Returns:
    str: The longest common substring.
    """
    
    # Initialize a 2D array, match[], with dimensions (m+1,n+1) 
    # where m is the length of string1 and n is the length of string2.
    m, n = len(string1), len(string2)
    match = [[0] * (n + 1) for _ in range(m + 1)]
    
    # Initialize variables maxLength to store the length of maximum substring found so far 
    # and endPos to store the ending index for longest common substring in string1.
    maxLength = 0
    endPos = 0
    
    # For i from 1 to m+1 loop through each character of string1:
    for i in range(1, m + 1):
        # For j from 1 to n+1 loop through each character of string2:
        for j in range(1, n + 1):
            # If the character at string1[i-1] is the same as the character at string2[j-1],
            if string1[i - 1] == string2[j - 1]:
                match[i][j] = match[i - 1][j - 1] + 1
                # If match[i][j] is greater than maxLength, assign match[i][j] to maxLength 
                # and i-1 to endPos.
                if match[i][j] > maxLength:
                    maxLength = match[i][j]
                    endPos = i
            # If the characters do not match, assign 0 to match[i][j].
            else:
                match[i][j] = 0
                
    # At the end of the nested loops, we have maxLength as the length of longest common substring. 
    # Retrieve the longest common substring from string1 using the endPos and maxLength.
    return string1[endPos - maxLength: endPos]