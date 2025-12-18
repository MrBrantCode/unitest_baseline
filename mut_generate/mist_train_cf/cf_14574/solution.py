"""
QUESTION:
Implement a function `title_case(sentence)` that converts a given sentence into title case, where all articles, prepositions, and coordinating conjunctions are lowercase unless they are the first or last word of the sentence. The function should also handle contractions and hyphenated words correctly. The input sentence is a string and the output should be a string in title case.
"""

def title_case(sentence):
    articles = ['a', 'an', 'the']
    prepositions = ['at', 'by', 'for', 'in', 'of', 'on', 'to', 'with']
    conjunctions = ['and', 'but', 'or', 'nor', 'so', 'for', 'yet']

    words = sentence.lower().split()
    titlecased_words = []

    for i, word in enumerate(words):
        if i == 0 or i == len(words) - 1:  
            titlecased_words.append(word.capitalize())
        elif '-' in word:  
            parts = word.split('-')
            titlecased_parts = [part.capitalize() for part in parts]
            titlecased_words.append('-'.join(titlecased_parts))
        elif word in articles + prepositions + conjunctions:  
            titlecased_words.append(word)
        else:
            titlecased_words.append(word.capitalize())

    return ' '.join(titlecased_words)