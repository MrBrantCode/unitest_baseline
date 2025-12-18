"""
QUESTION:
Write a function called `repeat_words_in_sentence` that takes two parameters: a string `sentence` and an integer `num`. The function should return a new sentence where each word in the original sentence is repeated `num` times in the same order.
"""

def repeat_words_in_sentence(sentence, num):
    words = sentence.split()
    result = []
    for word in words:
        result.extend([word]*num)
    return " ".join(result)