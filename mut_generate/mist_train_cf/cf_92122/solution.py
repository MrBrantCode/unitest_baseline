"""
QUESTION:
Write a function called `title_case_preserving_capitalization` that transforms a string from lowercase to title case while preserving the original capitalization of certain words. The function should follow these rules: the first letter of every word should be capitalized, articles, conjunctions, and prepositions should be lowercase unless they are the first or last word of the string, and words that are always capitalized should remain capitalized. The function should return the transformed string.
"""

def title_case_preserving_capitalization(string):
    lowercase_words = ['a', 'an', 'the', 'and', 'but', 'or', 'in', 'on', 'at', 'etc.']
    capitalized_words = ['I']
    words = string.lower().split()
    result = []
    
    for i, word in enumerate(words):
        if word in lowercase_words and i != 0 and i != len(words)-1:
            result.append(word)
        elif word in capitalized_words or word.isupper():
            result.append(word)
        else:
            result.append(word.capitalize())
    
    return ' '.join(result)