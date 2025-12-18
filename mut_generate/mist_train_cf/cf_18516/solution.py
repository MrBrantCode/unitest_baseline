"""
QUESTION:
Write a function named `reverse_words` that takes a string as input, reverses the order of its words, and returns the resulting string without any leading or trailing spaces.
"""

def reverse_words(input_str):
    # Split the input string into a list of words
    words = input_str.split()
    
    # Reverse the order of words
    words.reverse()
    
    # Join the words into a string
    output_str = ' '.join(words)
    
    return output_str.strip()