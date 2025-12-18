"""
QUESTION:
Create a function named `are_anagrams` that takes two parameters `word1` and `word2` and returns `True` if they are anagrams and `False` otherwise. Two words are considered anagrams if they contain the same letters, regardless of the order, case, or length.
"""

def are_anagrams(word1, word2):
    word1 = word1.lower()
    word2 = word2.lower()
    freq = {}
    
    for letter in word1:
        if letter not in freq:
            freq[letter] = 1
        else:
            freq[letter] += 1
    
    for letter in word2:
        if letter not in freq or freq[letter] == 0:
            return False
        freq[letter] -= 1
    
    return all(value == 0 for value in freq.values())