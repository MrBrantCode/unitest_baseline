"""
QUESTION:
Create a Python function `palindrome_freq` that takes a string `text` as input, calculates the occurrence rate of palindrome words, and returns this rate as a floating-point number. A palindrome word is a word that reads the same backward as forward. The function should split the input text into words and count the number of palindrome words. The occurrence rate is the ratio of palindrome words to the total number of words in the text. The function should return 0 if the input text is empty.
"""

def palindrome_freq(text):
    def is_palindrome(s):
        return s == s[::-1]

    words = text.lower().split()
    palindrome_count = sum(is_palindrome(word) for word in words)
    return palindrome_count / len(words) if words else 0