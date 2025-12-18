"""
QUESTION:
Write a function called `reverse_alphanumeric_words_in_string` that takes a string as input, reverses each word that consists only of alphanumeric characters, and returns the resulting string. Non-alphanumeric words should remain unchanged. The words in the output string should maintain their original order.
"""

def reverse_alphanumeric_words_in_string(string):
    def is_alphanumeric(word):
        return word.isalnum()
    
    def reverse_word(word):
        return word[::-1]
    
    words = string.split(' ')
    reversed_words = [reverse_word(word) if is_alphanumeric(word) else word for word in words]
    return ' '.join(reversed_words)