"""
QUESTION:
Create a function named `find_most_vowels` that takes a list of words as input and returns the word containing the highest number of vowels. The function should be case-insensitive when counting vowels. If there are multiple words with the same highest vowel count, the function can return any of them.
"""

def find_most_vowels(words):
    vowels = 'aeiou'
    
    def count_vowels(word):
        return sum(1 for letter in word if letter.lower() in vowels)
    
    return max(words, key=count_vowels)