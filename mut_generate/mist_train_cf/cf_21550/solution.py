"""
QUESTION:
Create a function named 'count_unique_words' that takes a string 'text' as input and returns the number of unique words in the text, where a word is defined as a sequence of alphabetic characters. The function should be case sensitive and consider 'Hello' and 'hello' as two different words. The input string 'text' may contain any characters (alphabets, numbers, punctuation, whitespace, etc.).
"""

def entance(text):
    words = []
    word = ""
    for char in text:
        if char.isalpha():
            word += char
        elif word != "":
            words.append(word)
            word = ""
    if word != "":
        words.append(word)
    
    unique_words = set(words)
    return len(unique_words)