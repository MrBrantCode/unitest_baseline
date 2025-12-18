"""
QUESTION:
Create a function named `capitalize_sentence` that takes a sentence as input and returns the sentence with the first letter of every word capitalized, excluding conjunctions ("and", "but"), prepositions ("of", "in"), and articles ("a", "an", "the"). The function should ignore the case of the input words when checking for exclusions.
"""

def capitalize_sentence(sentence):
    conjunctions = ["and", "but"]
    prepositions = ["of", "in"]
    articles = ["a", "an", "the"]
    
    words = sentence.split()
    capitalized_words = []
    
    for word in words:
        if word.lower() not in conjunctions and word.lower() not in prepositions and word.lower() not in articles:
            capitalized_words.append(word.capitalize())
        else:
            capitalized_words.append(word)
    
    capitalized_sentence = " ".join(capitalized_words)
    return capitalized_sentence