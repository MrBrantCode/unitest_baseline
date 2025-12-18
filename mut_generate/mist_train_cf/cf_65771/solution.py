"""
QUESTION:
Write a function called `is_anagram_of_palindrome` that takes a string as input and returns a boolean indicating whether the string is an anagram of a palindrome, ignoring case and non-alphanumeric characters. The function should be able to handle large datasets efficiently.
"""

def is_anagram_of_palindrome(input_string):
    input_string = input_string.lower()
    
    char_count = {}
    for char in input_string:
        if char.isalnum():
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1
    
    odd_counts = 0
    for count in char_count.values():
        if count % 2 != 0:
            odd_counts += 1

    return odd_counts <= 1