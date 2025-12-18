"""
QUESTION:
Write a function `longest_palindromic_substring(s)` that takes a character sequence `s` of up to 1000 characters as input and returns the longest palindromic substring. The function should have a time complexity less than O(n^2), where n is the length of the sequence.
"""

def longest_palindromic_substring(s):
    # Preprocess the input string
    t = '^#' + '#'.join(s) + '#$'
    n = len(t)
    
    # Initialize the array P
    P = [0] * n
    
    # Initialize the variables C and R
    C = 0
    R = 0
    
    # Iterate through each index of the input string
    for i in range(1, n - 1):
        # Check if the current index is within the rightmost boundary
        if i < R:
            # Use the mirror property to determine the minimum palindrome length at index i
            P[i] = min(P[2 * C - i], R - i)
        
        # Expand the palindrome centered at index i
        while t[i + P[i] + 1] == t[i - P[i] - 1]:
            P[i] += 1
        
        # Check if the expanded palindrome extends beyond the rightmost boundary
        if i + P[i] > R:
            R = i + P[i]
            C = i
    
    # Find the index with the maximum palindrome length
    maxLenIndex = P.index(max(P))
    
    # Extract the longest palindromic substring centered at maxLenIndex
    start = (maxLenIndex - P[maxLenIndex]) // 2
    end = start + P[maxLenIndex]
    return s[start:end]