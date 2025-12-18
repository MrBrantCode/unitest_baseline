"""
QUESTION:
Write a function named `repeat_words` that takes a string `sentence` and an integer `num` as input. The function should return a string where each word from the original sentence is repeated `num` times, maintaining the original word order, and the first letter of each word remains capitalized.
"""

def repeat_words(sentence, num):
    words = sentence.split()
    new_words = []
    for word in words:
        new_word = (word[0].upper() + word[1:].lower()) * num
        new_words.append(new_word)
    new_sentence = ' '.join(new_words)
    return new_sentence