"""
QUESTION:
Write a function `has_repeated_substring` that determines if a given string of length N contains a substring of length M (M < N) that repeats itself at least K (K > 1) times consecutively.
"""

def has_repeated_substring(s, M, K):
    """
    Determines if a given string contains a substring of length M that repeats itself at least K times consecutively.
    
    Parameters:
    s (str): The input string.
    M (int): The length of the substring.
    K (int): The number of times the substring should repeat.
    
    Returns:
    bool: True if the string contains a substring of length M that repeats at least K times consecutively, False otherwise.
    """
    N = len(s)
    if M >= N or K <= 1:
        return False
    
    for i in range(N - M + 1):
        sub1 = s[i:i+M]
        count = 1
        for j in range(i + 1, N - M + 1):
            sub2 = s[j:j+M]
            if sub1 == sub2:
                count += 1
                if count == K:
                    return True
            else:
                break
    return False