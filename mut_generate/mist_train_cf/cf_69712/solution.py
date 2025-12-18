"""
QUESTION:
Implement a function `validate_sentence(sentence: str) -> bool` that checks if a given sentence meets the following constraints:
- It starts with "This poet".
- It includes the phrase "one of America's".
- It ends with "loved poets."
Return `True` if the sentence is valid and `False` otherwise.
"""

def validate_sentence(sentence: str) -> bool:
    # validate if the sentence starts with "This poet".
    if not sentence.startswith('This poet'): 
        return False
    # validate if the sentence contains "one of America's".
    if 'one of America\'s' not in sentence: 
        return False
    # validate if the sentence ends with "loved poets."
    if not sentence.endswith('loved poets.'): 
        return False
    return True