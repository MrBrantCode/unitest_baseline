"""
QUESTION:
Create a function named `title_case_preserve` that transforms a string into title case while preserving the original capitalization of certain words. The function should follow these rules: 
- the first letter of every word should be capitalized, 
- articles, conjunctions, and prepositions should be lowercase unless they are the first or last word of the string, 
- any words that are always capitalized should remain capitalized, 
and the time complexity should be O(n), where n is the length of the string.
"""

def title_case_preserve(string):
    articles = ['a', 'an', 'the']
    conjunctions = ['and', 'but', 'or']
    prepositions = ['in', 'on', 'at', 'etc.']
    
    words = string.lower().split()
    
    for i, word in enumerate(words):
        if i == 0 or i == len(words) - 1:
            words[i] = word.capitalize()
        elif word not in articles and word not in conjunctions and word not in prepositions:
            words[i] = word.capitalize()
    
    return ' '.join(words)