"""
QUESTION:
Write a function called `reverse_words` that takes a string of letters and spaces as input, reverses the order of the words, and returns the result as a string. The function should not use any additional data structures (like lists, dictionaries, etc.) to store the characters or words, and should not use any built-in functions for string manipulation (like `reversed`, `split`, etc.).
"""

def reverse_words(sentence):
    # Convert the sentence string to a list of characters
    sentence = list(sentence)
    
    # Function to reverse a substring of the list
    def reverse_string(start, end):
        while start < end:
            sentence[start], sentence[end] = sentence[end], sentence[start]
            start += 1
            end -= 1
    
    # Reverse the entire sentence
    reverse_string(0, len(sentence) - 1)
    
    # Reverse each individual word in the reversed sentence
    start = 0
    for i in range(len(sentence)):
        if sentence[i] == ' ':
            reverse_string(start, i - 1)
            start = i + 1
    
    # Reverse the last word in the reversed sentence
    reverse_string(start, len(sentence) - 1)
    
    # Convert the list back to a string and return
    return ''.join(sentence)