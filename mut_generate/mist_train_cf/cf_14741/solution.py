"""
QUESTION:
Replace the first letter of each word in a given string with an underscore (_). The input string can contain multiple words separated by spaces and may include punctuation. Implement a function named `replace_first_letter` to accomplish this task. The function should take a string as input and return the modified string with the first letter of each word replaced.
"""

def replace_first_letter(string):
    words = string.split()
    replaced_words = []
    
    for word in words:
        replaced_word = "_" + word[1:]
        replaced_words.append(replaced_word)
    
    replaced_string = " ".join(replaced_words)
    return replaced_string