"""
QUESTION:
Write a function named `reverse_words` that takes a string as input and returns a new string where each word is reversed, while preserving the order of words and ignoring any punctuation marks and special characters. The function should not use any built-in string manipulation functions or libraries and must achieve a time complexity of O(n) and a space complexity of O(n), where n is the length of the input string.
"""

def reverse_words(string):
    # Create a list to store the reversed words
    reversed_words = []
    
    # Initialize variables to keep track of the start and end indices of each word
    start = None
    end = None
    
    # Iterate through each character in the string
    for i in range(len(string)):
        # Check if the current character is a letter
        if string[i].isalpha():
            # Set the start index of the word if it is not already set
            if start is None:
                start = i
            # Set the end index of the word
            end = i
        # If the current character is not a letter, it is a punctuation mark or special character
        else:
            # Check if a word has been found
            if start is not None:
                # Reverse the word and add it to the list
                reversed_words.append(string[start:end+1][::-1])
                # Reset the start and end indices
                start = None
                end = None
    
    # Check if a word has been found at the end of the string
    if start is not None:
        # Reverse the word and add it to the list
        reversed_words.append(string[start:end+1][::-1])
    
    # Initialize a variable to store the final reversed string
    reversed_string = ""
    
    # Iterate through the list of reversed words
    for i in range(len(reversed_words)):
        # Add the reversed word to the final string
        reversed_string += reversed_words[i]
        # Add a space after each word except the last one
        if i < len(reversed_words) - 1:
            reversed_string += " "
    
    return reversed_string