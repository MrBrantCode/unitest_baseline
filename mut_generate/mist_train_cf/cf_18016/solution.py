"""
QUESTION:
Write a function named `count_letters` that takes a string as input and returns a dictionary containing the frequency of each non-vowel letter in the string, ignoring case sensitivity and spaces. The input string will only contain lowercase letters and spaces.
"""

def count_letters(string):
    letter_count = {}
    vowels = set('aeiou')
    
    for letter in string.lower():
        if letter not in vowels and letter != ' ':
            letter_count[letter] = letter_count.get(letter, 0) + 1
                
    return letter_count