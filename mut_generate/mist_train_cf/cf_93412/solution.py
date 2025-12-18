"""
QUESTION:
Write a function named `reverse_words` that takes a string as input, reverses each word in the string, and returns the modified string. The function should not use any built-in string manipulation methods or libraries. The input string is assumed to have words separated by a single space character.
"""

def reverse_words(string):
    words = []
    word = ""
    
    for char in string:
        if char == " ":
            words.append(word)
            word = ""
        else:
            word += char
            
    if word:
        words.append(word)
        
    reversed_string = ""
    
    for word in words:
        reversed_word = ""
        for i in range(len(word)-1, -1, -1):
            reversed_word += word[i]
        reversed_string += reversed_word + " "
        
    return reversed_string.strip()