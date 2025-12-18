"""
QUESTION:
Write a function named `reverse_string` that takes a string as input and returns a new string where the order of words is reversed and each word's characters are also reversed. The function should not use any built-in string reversal functions or methods.
"""

def reverse_string(string):
    words = string.split()  # Split the string into a list of words
    reversed_words = []  # List to store the reversed words
    
    # Iterate over the list of words
    for word in words:
        # Reverse each word using a two-pointer approach
        start = 0
        end = len(word) - 1
        word_list = list(word)  # Convert the word to a list of characters
        
        # Swap characters at the two pointers until they meet in the middle
        while start < end:
            word_list[start], word_list[end] = word_list[end], word_list[start]
            start += 1
            end -= 1
        
        # Add the reversed word to the list
        reversed_words.append(''.join(word_list))
    
    # Join the reversed words using a space as the delimiter
    reversed_string = ' '.join(reversed(reversed_words))
    return reversed_string