"""
QUESTION:
Create a function named `count_vowels` that takes a string `s` as input and returns the total count of vowels (both lowercase and uppercase) present in the string. The function should be case-insensitive.
"""

def count_vowels(s):
    vowels = set("aeiouAEIOU")  
    return sum(1 for char in s if char in vowels)