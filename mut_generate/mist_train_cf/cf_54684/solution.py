"""
QUESTION:
Create a function named `reverse_odd(s: str)` that takes a string `s` as input and returns a new string where the characters at even index positions remain the same, and the characters at odd index positions are reversed. The function should handle strings of any length and should not modify the original string.
"""

def reverse_odd(s: str):
    even_chars = list(s[::2])   # list of characters at even indices
    odd_chars = list(s[1::2])   # list of characters at odd indices

    odd_chars.reverse()         # reverse the list of odd-indexed characters
    
    # Merge the two lists
    result = []
    for e, o in zip(even_chars, odd_chars + ['']):
        result.append(e)
        result.append(o)
        
    return ''.join(result)