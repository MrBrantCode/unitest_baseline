"""
QUESTION:
Write a function `duplicated_text(text, num)` that takes a string `text` and an integer `num` as input. The function should split `text` into sentences, duplicate each sentence `num` times, and return the resulting string with the original sentence order preserved. The sentences are separated by a period (`.`) and the resulting string should have a space between each sentence.
"""

def duplicated_text(text, num):
    sentences = [sent for sent in text.split('.') if sent]
    duplicated_sentences = [sent + '.' for sent in sentences for _ in range(num)]
    new_text = ' '.join(duplicated_sentences)
    return new_text