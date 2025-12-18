"""
QUESTION:
Create a function `sort_sentences_on_vowels()` that takes a list of sentences as input and returns the list sorted in descending order based on the number of vowels in each sentence. The function should be case-insensitive when counting vowels.
"""

def sort_sentences_on_vowels(sentences):
    def count_vowels(s):
        return sum([1 for c in s if c.lower() in 'aeiou'])
        
    sentences.sort(key=count_vowels, reverse=True)
    return sentences