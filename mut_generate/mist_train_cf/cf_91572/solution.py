"""
QUESTION:
Implement a function `reverse_words` that takes a string of lowercase and uppercase letters, spaces, and punctuation marks as input. The function should reverse the order of words in the string, maintaining the capitalization of the first letter of each word. The input string may contain multiple consecutive spaces and trailing spaces.
"""

def reverse_words(string):
    # Remove leading and trailing spaces
    string = string.strip()
    
    # Split the string into an array of words
    words = string.split()
    
    # Reverse the order of words
    words.reverse()
    
    # Capitalize the first letter of each word
    for i in range(len(words)):
        words[i] = words[i][0].capitalize() + words[i][1:]
    
    # Join the words back into a single string
    reversed_string = ' '.join(words)
    
    return reversed_string