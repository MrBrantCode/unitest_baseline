"""
QUESTION:
Create a function called `capitalize` that takes a sentence as input and returns the sentence with all words capitalized. The function should have a time complexity of O(n), where n is the number of characters in the sentence, and should not use any built-in string manipulation functions or regular expressions. The function should also use constant space complexity, meaning it should not create any additional data structures or variables, other than a variable to store the result.
"""

def capitalize(sentence):
    result = ""
    prev_char = ' '
    
    for char in sentence:
        if prev_char == ' ':
            result += char.upper()
        else:
            result += char
        
        prev_char = char
    
    return result