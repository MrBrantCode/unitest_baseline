"""
QUESTION:
Write a function called `recognize_programming_language` that recognizes the most likely programming language of a given code snippet based on its syntax, keywords, and variable naming conventions. The function should consider the frequency and order of specific keywords and symbols in the code snippet. The function should take a string `code` as input and return the most likely programming language. The function should support at least three programming languages: Python, JavaScript, and Java.
"""

from collections import Counter

def recognize_programming_language(code):
    keywords = {
        'python': {'def', 'import', 'for', 'if', 'else'},
        'javascript': {'function', 'import', 'for', 'if', 'else'},
        'java': {'public', 'class', 'import', 'for', 'if', 'else'},
        # Add more programming languages and their keywords here
    }

    # Variable naming conventions
    variable_naming_conventions = {
        'python': lambda word: word.islower(),
        'javascript': lambda word: word[0].islower(),
        'java': lambda word: word[0].islower(),
        # Add more programming languages and their variable naming conventions here
    }

    code_words = code.split()
    word_count = Counter(code_words)
    language_scores = {}

    for language, language_keywords in keywords.items():
        score = 0
        for word, count in word_count.items():
            if word in language_keywords:
                score += count
            if variable_naming_conventions[language](word):
                score += count * 0.5  # Adjust weight for variable naming
        language_scores[language] = score

    most_likely_language = max(language_scores, key=language_scores.get)
    return most_likely_language