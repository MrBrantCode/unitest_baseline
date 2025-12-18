"""
QUESTION:
Create a function `create_word_dict` that takes a list of words as input and returns a dictionary where keys are the words and values are tuples containing the number of letters, the number of vowels, and the number of unique letters in each word. 

Create another function `search_word_dict` that takes the dictionary and a word as input, and returns the tuple associated with the word if it exists in the dictionary, or a friendly error message if the word does not exist.
"""

def create_word_dict(word_list):
    word_dict = {}
    for word in word_list:
        num_letters = len(word)
        num_vowels = sum(1 for letter in word if letter.lower() in {'a', 'e', 'i', 'o', 'u'})
        num_unique = len(set(word))
        word_dict[word] = (num_letters, num_vowels, num_unique)
    return word_dict

def search_word_dict(word_dict, word):
    return word_dict.get(word, "Sorry, the word does not exist in the dictionary.")