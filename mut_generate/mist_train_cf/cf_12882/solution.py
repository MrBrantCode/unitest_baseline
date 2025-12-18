"""
QUESTION:
Write a function called `count_longer_words` that takes a string `sentence` and an integer `number` as inputs. The function should count and return the number of words in the sentence that are longer than the given number and only contain alphabetic characters (excluding any words with punctuation marks or numbers).
"""

def count_longer_words(sentence, number):
    count = 0
    words = sentence.split()
    for word in words:
        word = word.strip("',.?!:;\"")
        if word.isalpha() and len(word) > number:
            count += 1
    return count