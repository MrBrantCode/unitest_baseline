"""
QUESTION:
Create a function `contains_curse_word(sentence)` that takes a sentence as input and returns `True` if the sentence contains any curse words from a predefined list `curse_words` and `False` otherwise. The function should not use the `in` operator to check for curse words.
"""

def contains_curse_word(sentence):
    curse_words = ["curse1", "curse2", "curse3"]  # Add your own curse words here
    
    words = sentence.split()
    
    for word in words:
        for curse_word in curse_words:
            if word.lower() == curse_word.lower():
                return True
    
    return False