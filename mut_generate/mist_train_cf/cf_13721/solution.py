"""
QUESTION:
Write a function `capitalize_sentence` that takes a sentence as input and returns a new sentence where the first letter of every word is capitalized, excluding words that are conjunctions ("and", "but", "or", "nor", "for", "so", "yet").
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