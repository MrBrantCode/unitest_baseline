"""
QUESTION:
Create a function `reverse_words(string)` that takes a string as input and prints the string with the order of words reversed. The function should handle cases where there are multiple spaces between words or leading/trailing spaces, without using any built-in functions or methods to reverse the words or the string.
"""

def reverse_words(string):
    string = string.strip()
    reversed_words = []
    word = ""
    start_index = 0
    
    for i, char in enumerate(string):
        if char == " ":
            if word:
                reversed_words.append(word)
            word = ""
            start_index = i + 1
        else:
            word += char
    
    if word:
        reversed_words.append(word)
    
    reversed_string = " ".join(reversed_words[::-1])
    
    return reversed_string