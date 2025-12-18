"""
QUESTION:
Create a function `rewrite_sentence` that takes a string `text` as input. The function should replace the sentence "The decision was made by the president." with its active voice equivalent "The president made the decision." in the input string. The function should also return the number of words in the modified string and the number of times the word "president" appears in the original and rewritten sentences. The function should be able to handle input strings of any length and format.
"""

import re
def rewrite_sentence(text):
    # Find the sentence to rewrite
    match = re.search(r'The decision was made by the president\.', text)
    if not match:
        # Sentence not found, return original text
        return text, len(text.split()), text.count("president"), text.count("president")
    
    # Rewrite the sentence in the active voice
    active_voice = "The president made the decision."
    text = text[:match.start()] + active_voice + text[match.end():]
    
    # Count the number of words and "president" occurrences
    num_words = len(text.split())
    num_president_orig = 1  # Counting from the original sentence
    num_president_new = active_voice.count("president")
    
    return text, num_words, num_president_orig, num_president_new