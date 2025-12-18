"""
QUESTION:
Create a function called `word_count` that takes a string of words as input and returns a dictionary where the keys are the unique words and the values are the corresponding counts of occurrences of each word. The input string may contain multiple words separated by spaces.
"""

def word_count(string):
    word_dict = {}
    for word in string.split():
        if word in word_dict:
            word_dict[word] += 1
        else:
            word_dict[word] = 1

    return word_dict