"""
QUESTION:
Write a function named `vowel_count` that takes a string `text` as input and returns the total count of vowels in the string. The function should consider both lowercase and uppercase vowels ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U') and count duplicate vowels.
"""

def vowel_count(text):
    vowels = 'aeiouAEIOU'
    return sum(char in vowels for char in text)