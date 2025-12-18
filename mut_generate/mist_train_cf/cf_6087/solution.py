"""
QUESTION:
Write a function `check_word(word, letters)` that checks if a given word can be formed with a given set of letters, allowing for multiple uses of letters. The word must contain at least 5 letters, and the set of letters must contain at least 3 distinct letters. The function should return a boolean indicating whether the word can be formed and a list of minimum usage counts for each letter in the word.
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