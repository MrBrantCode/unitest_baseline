"""
QUESTION:
Write a function `longest_palindrome(s)` that finds the longest palindrome in a given string `s` of up to 10^6 characters. The function should have a time complexity of O(n) and a space complexity of O(1). If there are multiple palindromes of the same length, any one of them can be returned.
"""

def longest_palindrome(s):
    # Transform the input string to include a unique character
    # between each pair of characters to handle even-length palindromes
    transformed_s = "#".join(f"^{s}$")
    n = len(transformed_s)
    
    # Initialize the array to store the palindrome lengths
    P = [0] * n
    
    # Initialize the center and right boundaries of the current palindrome
    center = right = 0
    
    # Iterate through each character in the transformed string
    for i in range(1, n-1):
        # Find the mirror character position
        mirror = 2 * center - i
        
        # Check if the current character is within the right boundary
        if i < right:
            # Copy the length of the palindrome centered at the mirror character
            P[i] = min(right - i, P[mirror])
        
        # Expand around the current character to find the palindrome
        while transformed_s[i + (1 + P[i])] == transformed_s[i - (1 + P[i])]:
            P[i] += 1
        
        # Check if the palindrome centered at the current character extends beyond the right boundary
        if i + P[i] > right:
            center = i
            right = i + P[i]
    
    # Find the longest palindrome length and its center position
    max_len = max(P)
    center_idx = P.index(max_len)
    
    # Extract the longest palindrome from the original string
    start = (center_idx - max_len) // 2
    end = start + max_len
    
    return s[start:end]