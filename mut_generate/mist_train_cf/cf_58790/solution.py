"""
QUESTION:
Create a function named `combine_phrases` that accepts two lists: `phrases` and `punctuations`. The function should combine the phrases into a single sentence, separating them with punctuation marks from the `punctuations` list in the order they appear. If there are more phrases than punctuation marks, the function should loop through the `punctuations` list to continue the pattern. The function should handle cases where either `phrases` or `punctuations` (or both) are empty.
"""

from itertools import cycle

def combine_phrases(phrases, punctuations):
    if len(phrases) == 0:
        return ''
    elif len(punctuations) == 0:
        return ' '.join(phrases)
    else:
        punctuation_cycle = cycle(punctuations) 
        result = ''
        for phrase, punctuation in zip(phrases, punctuation_cycle):
            result += phrase + punctuation + ' '
        return result.strip()