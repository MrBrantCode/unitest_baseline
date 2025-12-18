"""
QUESTION:
Write a function `sort_words_by_vowels` that takes a string of words as input, removes any duplicate words, and returns a list of unique words sorted in descending order based on the number of vowels present in each word.
"""

def sort_words_by_vowels(s):
    words = s.split()
    words = list(set(words))
    
    def count_vowels(word):
        vowels = 'aeiouAEIOU'
        count = 0
        for char in word:
            if char in vowels:
                count += 1
        return count

    words.sort(key=count_vowels, reverse=True)
    return words