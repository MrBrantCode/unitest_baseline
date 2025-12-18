"""
QUESTION:
Write a function named `filter_paragraphs` that takes a list of strings `paragraphs` as input. The function should return a list of strings where each string has 10 words or less, does not contain any numbers, and is in lower case.
"""

def filter_paragraphs(paragraphs):
    def has_numbers(inputString):
        return any(char.isdigit() for char in inputString)
    
    filtered_paragraphs = [sentence.lower() for sentence in paragraphs if len(sentence.split()) <= 10 and not has_numbers(sentence)]
    
    return filtered_paragraphs