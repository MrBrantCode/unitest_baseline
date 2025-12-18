"""
QUESTION:
Write a function `compare_strings(s1, s2)` to compare two strings `s1` and `s2` using only bitwise operations. The function should have a time complexity of O(n), where n is the length of the longer string, and use a constant amount of additional space.
"""

def compare_strings(s1, s2):
    # Find the length of the longer string
    n = max(len(s1), len(s2))
    
    # Compare the strings character by character using bitwise XOR
    for i in range(n):
        # Use bitwise XOR to compare the characters
        if i < len(s1) and i < len(s2):
            if ord(s1[i]) ^ ord(s2[i]):
                return False
        else:
            # If the strings have different lengths, return False
            return False
    
    # If all characters match, return True
    return True