"""
QUESTION:
Write a function `findLongestPalindrome(s)` to find the longest palindrome in a given string `s` of maximum length 10^6 characters. The function should return the longest palindrome found in the string with a time complexity of O(n). If there are multiple palindromes of the same length, any one of them can be returned.
"""

def findLongestPalindrome(s):
    # Preprocess the string
    processedString = '#' + '#'.join(s) + '#'
    n = len(processedString)
    
    # Initialize variables
    P = [0] * n
    center = right = 0
    maxLen = 0
    maxCenter = 0
    
    # Iterate through the preprocessed string
    for i in range(n):
        # Calculate the mirror position
        mirror = 2 * center - i
        
        # Check if the current position is within the rightmost palindrome
        if i < right:
            P[i] = min(right - i, P[mirror])
        
        # Attempt to expand the palindrome centered at the current position
        while i - P[i] - 1 >= 0 and i + P[i] + 1 < n and processedString[i - P[i] - 1] == processedString[i + P[i] + 1]:
            P[i] += 1
        
        # Update the rightmost position and the center if necessary
        if i + P[i] > right:
            center = i
            right = i + P[i]
        
        # Track the longest palindrome seen so far
        if P[i] > maxLen:
            maxLen = P[i]
            maxCenter = i
    
    # Extract the longest palindrome from the original string
    start = (maxCenter - maxLen) // 2
    end = start + maxLen
    return s[start:end]