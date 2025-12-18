"""
QUESTION:
Create a function `is_palindrome(input_string)` that takes a string as input, removes all non-alphanumeric characters, converts it to lowercase, and returns `True` if the resulting string is the same when reversed, and `False` otherwise.
"""

def is_palindrome(input_string):
    # remove unwanted characters by only retaining alphanumerics, replace spaces with nothing and convert to lower case
    cleaned_string = ''.join(e for e in input_string if e.isalnum()).lower()

    # Here, we check if the cleaned string is equal to its reverse
    return cleaned_string == cleaned_string[::-1]