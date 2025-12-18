"""
QUESTION:
Write a function `extract_permissions(text)` that takes a string of license agreement text as input and returns two sets of unique words: one for verbs and one for nouns. The input string contains a series of permissions separated by commas, with each permission being a combination of verbs and nouns separated by spaces. The function should categorize words as verbs or nouns based on whether they end with 's' (nouns) or not (verbs).
"""

def extract_permissions(text):
    verbs = set()
    nouns = set()
    
    permissions = text.split(',')
    for permission in permissions:
        words = permission.strip().split()
        for word in words:
            if word.isalpha():
                if word.endswith('s'):
                    nouns.add(word)
                else:
                    verbs.add(word)
    
    return verbs, nouns