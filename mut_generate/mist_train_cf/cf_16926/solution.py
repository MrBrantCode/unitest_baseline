"""
QUESTION:
Create a function named `are_anagrams` that takes two string parameters `word1` and `word2`. This function should determine if `word1` and `word2` are anagrams of each other, considering different letter cases and lengths. The function should return `True` if `word1` and `word2` are anagrams, and `False` otherwise.
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