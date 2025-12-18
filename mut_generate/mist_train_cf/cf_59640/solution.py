"""
QUESTION:
Write a function called `reverse_words` that takes a string as input and returns the string with the words in reverse order, but the characters within each word remaining in the same order. The function should not use any built-in functions or methods. If the input is not a string, the function should return "Error: Input is not a string".
"""

def reverse_words(input_string):
    # Error handling for non-string inputs
    if not isinstance(input_string, str):
        return "Error: Input is not a string"

    temp_word = '' 
    reverse_string = ''  
    for i in range(len(input_string)):
        if input_string[i] != ' ':  
            temp_word += input_string[i] 
        else:
            reverse_string = ' ' + temp_word + reverse_string
            temp_word = ''
    # appending the last word
    reverse_string = temp_word + reverse_string 

    return reverse_string