"""
QUESTION:
Reverse every other word in a given string, then return the string. Throw away any leading or trailing whitespace, while ensuring there is exactly one space between each word. Punctuation marks should be treated as if they are a part of the word in this kata.
"""

def reverse_alternate_words(input_string: str) -> str:
    # Split the input string into words
    words = input_string.split()
    
    # Reverse every other word
    reversed_words = [
        word[::-1] if i % 2 != 0 else word
        for i, word in enumerate(words)
    ]
    
    # Join the words back into a single string with a single space between each word
    result = ' '.join(reversed_words)
    
    return result