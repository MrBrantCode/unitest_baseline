"""
QUESTION:
Implement a function `manacher` to find the longest palindrome in a given string. The function should take a string `s` as input and return the longest palindrome substring. The algorithm should achieve linear time complexity.
"""

def manacher(s: str) -> str:
    """
    This function finds the longest palindrome in a given string using Manacher's Algorithm.
    
    Args:
    s (str): The input string.
    
    Returns:
    str: The longest palindrome substring.
    """
    T = '#'.join('^{}$'.format(s))  # Preprocess the string by inserting special characters
    n = len(T)
    P = [0] * n  # Array to store the length of the palindrome
    C = R = 0  # Center and right boundary of the current palindrome
    
    for i in range(1, n-1):
        P[i] = (R > i) and min(R - i, P[2*C - i])  # Calculate the length of the palindrome
        # Attempt to expand the palindrome centered at i
        while T[i + 1 + P[i]] == T[i - 1 - P[i]]:
            P[i] += 1

        # If the palindrome centered at i expand past R,
        # adjust center based on expanded palindrome.
        if i + P[i] > R:
            C, R = i, i + P[i]
    
    # Find the maximum element in P.
    maxLen, centerIndex = max((n, i) for i, n in enumerate(P))
    return s[(centerIndex  - maxLen)//2: (centerIndex  + maxLen)//2]