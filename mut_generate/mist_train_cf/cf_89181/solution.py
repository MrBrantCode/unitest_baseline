"""
QUESTION:
Create a function `convert_sentence_to_list` that takes a sentence as input, excludes any words that start with a vowel and contain more than three letters, and returns the remaining words in a list sorted in alphabetical order. The function should have a time complexity of O(nlogn), where n is the number of words in the sentence.
"""

def convert_sentence_to_list(sentence):
    vowels = ['a', 'e', 'i', 'o', 'u']
    words = []
    sentence_words = sentence.split()

    for word in sentence_words:
        if word[0].lower() not in vowels and len(word) <= 3:
            words.append(word)

    return sorted(words)