"""
QUESTION:
Create a function named `reverse_even` that takes a string `s` as input and returns a new string where the characters at even indices are reversed in order, while characters at odd indices remain unchanged. The function should handle strings of any length, including those with an odd or even number of characters.
"""

def reverse_even(s: str) -> str:
    if len(s) < 2:
        return s
    
    even_chars = []
    odd_chars = []
    
    for i in range(len(s)):
        if i % 2 == 0:
            even_chars.append(s[i])
        else:
            odd_chars.append(s[i])
    
    even_chars.reverse()
    
    result = []
    for e, o in zip(even_chars, odd_chars):
        result.append(e)
        result.append(o)
    
    if len(even_chars) > len(odd_chars):
        result.append(even_chars[-1])
    elif len(odd_chars) > len(even_chars):
        result.append(odd_chars[-1])
    
    return ''.join(result)