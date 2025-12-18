"""
QUESTION:
Write a function named `check_word` that takes a string `word` and a list of characters `letters` as input, and returns a boolean value indicating whether the word can be formed from the given letters, as well as a list of the minimum number of times each letter in the set needs to be used to form the word. The function should only consider words with at least 5 letters and sets of letters with at least 3 distinct letters. The letters in the set can be used multiple times to form the word.
"""

def check_word(word, letters):
    if len(word) < 5 or len(set(letters)) < 3:
        return False, []
    
    # Count the occurrences of each letter in the set
    letter_count = {}
    for letter in letters:
        letter_count[letter] = letter_count.get(letter, 0) + 1
    
    # Check if each letter in the word can be formed
    letter_usage = {}
    for letter in word:
        if letter not in letter_count or letter_count[letter] == 0:
            return False, []
        letter_count[letter] -= 1
        letter_usage[letter] = letter_usage.get(letter, 0) + 1
    
    # Check if all required letters have been used at least once
    for letter, count in letter_usage.items():
        if count == 0:
            return False, []
    
    return True, letter_usage.values()