"""
QUESTION:
Write a function `avg_word_length(sentence)` that calculates the average word length of a sentence containing both English and Spanish words, excluding prepositions, conjunctions, and articles in both languages. The function should take a sentence as input and return the average word length as a floating point number. Assume that the input sentence only contains alphabetic characters and spaces, and words are separated by single spaces.
"""

def avg_word_length(sentence):
    english_prepositions = ["of", "in", "to", "for", "with", "on", "at", "from", "by", "about", "as", "into", "like", "through", "after", "over", "between", "out", "against", "during", "without", "before", "under", "around", "among"]
    spanish_prepositions = ["de", "en", "a", "para", "con", "por", "sobre", "tras", "entre", "sin", "hacia", "desde", "durante", "bajo", "ante", "sobre", "dentro", "fuera", "según", "contra", "mediante", "sino", "alrededor", "entre"]
    prepositions = english_prepositions + spanish_prepositions
    articles = ["the", "a", "an", "el", "la", "los", "las", "un", "una", "unos", "unas"]
    conjunctions = ["and", "or", "but", "yet", "so", "ni", "o", "pero", "sin embargo", "así que"]
    excluded_words = prepositions + articles + conjunctions
    words = sentence.split()
    total_length = 0
    count = 0
    for word in words:
        if word.lower() not in excluded_words:
            total_length += len(word)
            count += 1
    if count == 0:
        return 0
    else:
        return total_length / count