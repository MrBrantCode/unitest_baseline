"""
QUESTION:
Write a function `reverse_words_in_string` that takes a string as input and returns a new string where each word is reversed. The function should not use any built-in reverse functions or slicing. It should treat punctuation as part of the words and handle white spaces efficiently.
"""

def reverse_words_in_string(input_string):
    # Split the input string into a list of words
    words = input_string.split()
    
    # Initialize a list to store the reversed words
    reversed_words = []
    
    # For each word in the original list
    for word in words:
        
        # Initialize an empty string to store the reversed word
        reversed_word = ''
        
        # Use a loop to iterate the characters in the word from last to first
        for char in range(len(word) - 1, -1, -1):
            
            # Append each character to the reversed word
            reversed_word += word[char]
        
        # Append the reversed word to the list of reversed words
        reversed_words.append(reversed_word)
    
    # Join the reversed words with spaces to form a string
    reversed_string = ' '.join(reversed_words)
    
    return reversed_string