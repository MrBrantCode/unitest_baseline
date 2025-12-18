"""
QUESTION:
Write a function called `remove_vowels_and_special_chars` that takes a string as input and returns a string containing only alphanumeric characters that are not vowels. The output string should not contain any vowels (both lowercase and uppercase) and non-alphanumeric characters.
"""

def remove_vowels_and_special_chars(text):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']  
    result = [char for char in text if char.isalnum() and char not in vowels]  
    return ''.join(result)