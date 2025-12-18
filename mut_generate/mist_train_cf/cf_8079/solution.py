"""
QUESTION:
Write a Python function called `correct_likes` that takes a sentence as input, uses regular expressions to match and correct all instances of the word "likes" to its past tense form ("liked") if the subject of the sentence is singular or to the same form ("likes") if the subject is plural, and returns the corrected sentence while maintaining proper grammar and punctuation throughout.
"""

import re

def correct_likes(sentence):
    # Define a regular expression pattern to match the word "likes" after a subject noun
    pattern = re.compile(r'(\w+)\s+(likes)')
    
    # Define a function to determine whether a subject is singular or plural
    def get_subject_verb_agreement(match):
        subject = match.group(1)
        # If the subject ends with 's', it's likely plural
        if subject.endswith('s'):
            return match.group(0)
        else:
            return subject + ' liked'
    
    # Use the sub() function to replace each match with its corrected form
    corrected_sentence = re.sub(pattern, get_subject_verb_agreement, sentence)
    
    return corrected_sentence