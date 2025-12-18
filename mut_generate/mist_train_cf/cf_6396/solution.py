"""
QUESTION:
Write a function `correct_sentence` that takes an input string representing a sentence and returns the sentence with correct structure. The returned sentence should not exceed 15 words and all words should be in their proper tense and form.
"""

def correct_sentence(sentence):
    words = sentence.split()
    if len(words) > 15:
        words = words[:15]
    corrected_sentence = ' '.join(words)
    if not corrected_sentence.endswith('.'):
        corrected_sentence += '.'
    return corrected_sentence.capitalize()