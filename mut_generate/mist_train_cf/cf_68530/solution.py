"""
QUESTION:
Create a function `unique_palindrome_counter` that takes a string of text as input and returns the count of unique palindrome words in the text. The function should split the text into words, check each word for palindrome, and ignore duplicates.
"""

def unique_palindrome_counter(text):
    # Function which checks if a word is a palindrome or not
    def is_palindrome(word):
        return word == word[::-1]

    # Split the text into words
    words = text.split()
    palindromes = set()

    # Iterate over the words and check if they are palindrome
    for word in words:
        if is_palindrome(word):
            # Add to the set if it's a palindrome
            palindromes.add(word)
            
    # return the number of unique palindromes
    return len(palindromes)