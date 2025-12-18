"""
QUESTION:
Design a function named `character_search` that takes two parameters: `sentence` and `target_string`. The function should return `True` if `target_string` is found in `sentence`, and `False` otherwise.
"""

def character_search(sentence, target_string):
    if target_string in sentence:
        return True
    else:
        return False