"""
QUESTION:
Create a function called `replace_fifth_occurrence` that takes two arguments: a target word and a text string. The function should replace every fifth occurrence of the target word in the text with an asterisk symbol, ignoring non-word characters and treating words with punctuation as distinct from the same word without punctuation. The comparison of the target word with words in the text should be case-insensitive.
"""

def replace_fifth_occurrence(word, text):
    words = text.split()
    counter = 0
    for i in range(len(words)):
        if words[i].lower().strip('.,!?;:"\'').replace("'s", "") == word.lower():
            counter += 1
            if counter % 5 == 0:
                words[i] = '*'
    return ' '.join(words)