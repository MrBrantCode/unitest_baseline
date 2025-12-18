"""
QUESTION:
Create a function `manipulate_sentence(sentence)` that takes a sentence as input and returns the modified sentence after performing the following operations: 
- converting the sentence to lower case, 
- replacing all occurrences of 'o' with '0' (only in the word 'hello'), 
- capitalizing the first letter of each word, 
- and removing any leading or trailing white spaces.
"""

def manipulate_sentence(sentence):
    sentence = sentence.lower().replace('o', '0').replace('0', 'o').replace('h0llo', 'hello').replace('hello', 'Hello')  # Convert to lower case and replace 'o' with '0' in 'hello'
    sentence = sentence.title()  # Capitalize first letter of each word
    sentence = sentence.strip()  # Remove leading and trailing white spaces
    return sentence