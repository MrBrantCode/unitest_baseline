"""
QUESTION:
Write a function named `capitalize_words_except_specific_words` that takes a string as input, capitalizes all words in the string except for the words "and" and "the", and returns the modified string. The function should be case-insensitive when excluding the words "and" and "the".
"""

def capitalize_words_except_specific_words(string):
    words = string.split()  
    capitalized_words = []  

    for word in words:
        if word.lower() in ["and", "the"]:  
            capitalized_words.append(word)  
        else:
            capitalized_words.append(word.capitalize())  

    return ' '.join(capitalized_words)  