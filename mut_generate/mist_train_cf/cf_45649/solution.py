"""
QUESTION:
Write a function `reverse_even(s: str)` that takes a string `s` and returns a new string where characters at even index positions are reversed in order, while characters at odd index positions remain unchanged.
"""

def reverse_even(s: str) -> str:
    even_chars = [s[i] for i in range(0,len(s),2)][::-1]    # Get the characters at even index and reverse them
    list_s = list(s)    # Convert string to list
    list_s[::2] = even_chars   # Replace the elements at the even index with reversed elements
    return ''.join(list_s)    # Convert list back to string