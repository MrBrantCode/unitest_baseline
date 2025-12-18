"""
QUESTION:
Create a function `find_max` that takes a list of words and an integer `m` as input. For each word in the list, count the frequency of each character and store it in a dictionary. Then, filter out the words with more than `m` unique characters. Return a list of tuples, where each tuple contains a word and its corresponding character frequency dictionary.
"""

def find_max(words, m): 
    word_dicts = [(word, {char: word.count(char) for char in word}) for word in words]
    word_dicts = [word_tuple for word_tuple in word_dicts if len(word_tuple[1]) <= m] 
    return word_dicts