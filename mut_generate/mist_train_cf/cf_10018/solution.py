"""
QUESTION:
Write a function named `word_count` that takes a sentence as input and returns a dictionary containing unique words and their counts. The function should be case-insensitive and ignore punctuation marks. The function should have a time complexity of O(n), where n is the length of the sentence, and should not use any built-in functions or libraries that directly solve the problem.
"""

def word_count(sentence):
    word_dict = {}
    word = ""
    for char in sentence:
        if char.isalpha():
            word += char.lower()
        elif word != "":
            if word in word_dict:
                word_dict[word] += 1
            else:
                word_dict[word] = 1
            word = ""
    if word != "":
        if word in word_dict:
            word_dict[word] += 1
        else:
            word_dict[word] = 1
    return word_dict