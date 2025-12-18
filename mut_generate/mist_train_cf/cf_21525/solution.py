"""
QUESTION:
Create a function `capitalize_sentence(sentence)` that takes a string sentence as input, capitalizes the first letter of every word excluding conjunctions and prepositions, and returns the modified sentence. The conjunctions and prepositions to be excluded are: 
- Conjunctions: "and", "but", "or", "nor", "for", "yet", "so"
- Prepositions: "of", "in", "on", "at", "by", "from", "to", "with", "over", "under", "below", "above", "into", "onto", "through", "towards", "onto", "after", "before", "between", "among"
"""

def capitalize_sentence(sentence):
    conjunctions = ["and", "but", "or", "nor", "for", "yet", "so"]
    prepositions = ["of", "in", "on", "at", "by", "from", "to", "with", "over", "under", "below", "above", "into", "onto", "through", "towards", "onto", "after", "before", "between", "among"]

    words = sentence.split()
    capitalized_words = []

    for word in words:
        if word.lower() not in conjunctions and word.lower() not in prepositions:
            capitalized_words.append(word.capitalize())
        else:
            capitalized_words.append(word.lower())

    capitalized_sentence = " ".join(capitalized_words)
    return capitalized_sentence