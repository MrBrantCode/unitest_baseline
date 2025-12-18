"""
QUESTION:
Create a function `find_palindromes_in_text` that takes a string of text as input, ignoring punctuation and case sensitivity, and returns the number of palindrome words in the text.
"""

def find_palindromes_in_text(input_text):
    # Remove punctuation and convert to lower case
    cleaned_text = ''.join(e for e in input_text if e.isalnum() or e.isspace()).lower()
    
    # Split cleaned_text into words
    words = cleaned_text.split(' ')
    
    # Initialize counter
    palindrome_count = 0

    # For each word, check if it's a palindrome
    for word in words:
        if word == word[::-1]:     # If word remains the same when reversed
            palindrome_count += 1

    return palindrome_count