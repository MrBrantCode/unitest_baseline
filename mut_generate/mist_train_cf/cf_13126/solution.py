"""
QUESTION:
Construct a function named `check_hello` that takes a string as input and returns a tuple containing a boolean value indicating whether the string contains the word "hello" (case-insensitive) and an integer representing the number of times the word "hello" appears in the string. The function should be case-insensitive and should return the correct output for strings containing multiple occurrences of "hello" in different cases.
"""

def check_hello(string):
    # Convert the string and the word "hello" to lowercase
    lowercase_string = string.lower()
    lowercase_word = "hello"

    # Check if the lowercase string contains the lowercase word
    contains_hello = lowercase_word in lowercase_string

    # Count the number of times the word "hello" appears in the string
    count_hello = lowercase_string.count(lowercase_word)

    return contains_hello, count_hello