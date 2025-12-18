"""
QUESTION:
Create a function `capitalize_sentence(sentence)` that capitalizes the first letter of every word in a sentence, excluding conjunctions. The function should take a string `sentence` as input and return a string where the first letter of every word is capitalized, except for conjunctions which should be left in lowercase. Conjunctions include "and", "but", "or", "nor", "for", "so", and "yet".
"""

def capitalize_sentence(sentence):
    conjunctions = ["and", "but", "or", "nor", "for", "so", "yet"]
    words = sentence.split()
    capitalized_words = []
    
    for word in words:
        if word.lower() not in conjunctions:
            capitalized_words.append(word.capitalize())
        else:
            capitalized_words.append(word)
    
    capitalized_sentence = " ".join(capitalized_words)
    return capitalized_sentence