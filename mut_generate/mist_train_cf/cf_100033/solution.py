"""
QUESTION:
Write a function `avg_word_length(sentence)` that calculates the average word length of a sentence containing both English and Spanish words. The function should exclude prepositions, conjunctions, and articles in both languages from the calculation.
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