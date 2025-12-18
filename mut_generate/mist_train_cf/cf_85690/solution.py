"""
QUESTION:
Write a function `count_e` that takes a string as input and returns the number of times the letter 'e' (both upper and lower case) appears in the string. The function should be case-insensitive and efficient for strings up to a length of 100,000 characters.
"""

def count_e(my_string):
    my_string_lower = my_string.lower()  # Convert the input string to lowercase.
    count = my_string_lower.count('e')  # Count the number of 'e's in the lowercase string.
    return count