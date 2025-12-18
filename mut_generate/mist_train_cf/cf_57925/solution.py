"""
QUESTION:
Create a function `replace_nth_occurrence` that takes in two parameters: `text_string` and `word_dict`. The function replaces every nth occurrence of a specific word in `text_string` with a given term as specified in `word_dict`. The word counting should be case-insensitive, but the case of the original word should be respected in the replacement term. Punctuation attached to words should affect their counting. The `word_dict` is a dictionary where keys are target words and values are tuples of replacement frequency and replacement word.
"""

def replace_nth_occurrence(text_string, word_dict):
    words = text_string.split()
    word_counts = {}
    for i, word in enumerate(words):
        for target, (n, replacement) in word_dict.items():
            clean_word = word.lower().strip(",.!?;:'\"-")
            if clean_word == target:
                word_counts[clean_word] = word_counts.get(clean_word, 0) + 1
                if word_counts[clean_word] % n == 0:
                    if word.istitle():
                        words[i] = replacement.capitalize()
                    else:
                        words[i] = replacement
    return ' '.join(words)