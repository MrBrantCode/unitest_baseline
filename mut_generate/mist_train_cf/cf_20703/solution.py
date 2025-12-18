"""
QUESTION:
Write a function `reverse_words` that takes a sentence as input and returns a new sentence where each word containing at least one vowel is reversed. The function should not use any built-in string manipulation functions or methods and have a time complexity of O(n), where n is the length of the input sentence.
"""

def reverse_words(sentence):
    vowels = set('aeiouAEIOU')
    words = sentence.split()
    reversed_words = []
    
    for word in words:
        if any(char in vowels for char in word):
            reversed_word = ''
            i = len(word) - 1
            while i >= 0:
                reversed_word += word[i]
                i -= 1
            reversed_words.append(reversed_word)
        else:
            reversed_words.append(word)
    
    reversed_sentence = ' '.join(reversed_words)
    return reversed_sentence