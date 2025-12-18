"""
QUESTION:
Create a function named `extract_words(sentence, letter)` that takes a sentence and a letter as arguments. The function should return a list of words from the sentence that start with the specified letter (case-insensitive) and have a length of 3 or more characters.
"""

def extract_words(sentence, letter):
    words = sentence.split()
    result = []
    
    for word in words:
        if word[0].upper() == letter.upper() and len(word) >= 3:
            result.append(word)
    
    return result