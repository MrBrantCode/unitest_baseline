"""
QUESTION:
Create a function called `is_substring` that checks if a given string `s2` is a substring of another string `s1` with at least 3 characters between occurrences. The function should be case-sensitive and ignore leading and trailing whitespaces in both `s1` and `s2`. It should return `True` if `s2` is a substring of `s1` and `False` otherwise. The function should handle empty strings as inputs, special characters, and numbers in both `s1` and `s2`.
"""

def is_substring(s1, s2):
    # Ignore leading and trailing whitespaces
    s1 = s1.strip()
    s2 = s2.strip()
    
    # Check if s1 or s2 is empty
    if s1 == "" or s2 == "":
        return False
    
    # Iterate through s1 to find occurrences of s2
    i = 0
    while i < len(s1):
        if s1[i:i+len(s2)] == s2:
            # Check if there are at least 3 characters between occurrences
            if i > 0 and s1[i-1] != " " and s1[i-1].isalpha():
                return False
            if i+len(s2) < len(s1) and s1[i+len(s2)] != " " and s1[i+len(s2)].isalpha():
                return False
            return True
        i += 1
    
    return False