"""
QUESTION:
Write a function `reverse_even(s)` that takes a string `s` as input and returns a modified string where characters at even indices are reversed in order, while characters at odd indices remain unchanged.
"""

def reverse_even(s: str):
    even_chars = s[::2][::-1]
    output = ''
    even_index = 0
    
    for i in range(len(s)):
        if i % 2 == 0:
            output += even_chars[even_index]
            even_index += 1
        else:
            output += s[i]
            
    return output