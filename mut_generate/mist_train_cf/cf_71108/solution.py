"""
QUESTION:
Write a function `replicate_words` that takes a string `text` and an integer `number` as inputs. The function should return a modified string where each word in the original text is repeated `number` times.
"""

def replicate_words(text, number):
    words = text.split()
    replicated_words = [word * number for word in words]
    return ' '.join(replicated_words)