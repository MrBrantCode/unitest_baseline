"""
QUESTION:
Reverse the order of words in a given string using a time complexity of O(n) and a space complexity of O(1). Implement the solution using a function named `reverse_words(s)`, where `s` is the input string, without using built-in string reversal functions.
"""

def reverse_words(s):
    # Convert the string into a character array
    char_array = list(s)
    
    # Reverse the entire character array
    start = 0
    end = len(char_array) - 1
    while start < end:
        char_array[start], char_array[end] = char_array[end], char_array[start]
        start += 1
        end -= 1
    
    # Reverse each word separately
    def reverse_word(char_array, start, end):
        while start < end:
            char_array[start], char_array[end] = char_array[end], char_array[start]
            start += 1
            end -= 1
    
    start = 0
    for i in range(len(char_array)):
        if char_array[i] == ' ':
            reverse_word(char_array, start, i - 1)
            start = i + 1
    
    # Reverse the last word
    reverse_word(char_array, start, len(char_array) - 1)
    
    # Convert the character array back to a string
    reversed_string = ''.join(char_array)
    return reversed_string