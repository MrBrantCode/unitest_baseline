"""
QUESTION:
Write a function named `reverse_words` that takes a string of words separated by spaces as input and returns a new string with the order of the words reversed. The function should not use any built-in string manipulation functions and should have a time complexity of O(n) and space complexity of O(1), where n is the length of the string.
"""

def reverse_words(string):
    # Step 1: Reverse the entire string
    string = reverse_string(string, 0, len(string)-1)
    
    # Step 2: Reverse each individual word
    start = 0
    for i in range(len(string)):
        if string[i] == ' ':
            string = reverse_string(string, start, i-1)
            start = i + 1
    
    # Step 3: Reverse the characters of each individual word back to their original order
    string = reverse_string(string, start, len(string)-1)
    
    return string

def reverse_string(string, start, end):
    string = list(string)  # Convert the string to a list to modify it
    while start < end:
        string[start], string[end] = string[end], string[start]  # Swap the characters
        start += 1
        end -= 1
    return ''.join(string)  # Convert the list back to a string