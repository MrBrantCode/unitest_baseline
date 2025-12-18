"""
QUESTION:
Write a function `remove_duplicates(sentence)` that takes a sentence as input and returns a modified sentence where any duplicate words are removed, except for the first occurrence of each word. The words in the sentence may be separated by spaces and may contain punctuation.
"""

def remove_duplicates(sentence):
    words = sentence.split()
    cleaned_sentence = []
    for word in words:
        if word.strip('.,!?"\'') not in [x.strip('.,!?"\'') for x in cleaned_sentence]:
            cleaned_sentence.append(word)
    return ' '.join(cleaned_sentence)