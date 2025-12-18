"""
QUESTION:
Write a function named `most_frequent_word` that finds the most frequently used word in a given text. The function should ignore special characters, be case insensitive, and not use any built-in string or regular expression functions. The function must use a helper function named `is_letter_or_number` to identify if a character is a letter (A-Z, a-z) or a number (0-9).
"""

def is_letter_or_number(char):
    return ('a' <= char <= 'z') or ('A' <= char <= 'Z') or ('0' <= char <= '9')

def most_frequent_word(text):
    word_frequencies = {}
    curr_word = ''
    for char in text:
        if is_letter_or_number(char):
            curr_word += char.lower()  
        else:
            if curr_word:  
                if curr_word in word_frequencies:
                    word_frequencies[curr_word] += 1
                else:
                    word_frequencies[curr_word] = 1
                curr_word = ''  
    if curr_word:
        if curr_word in word_frequencies:
            word_frequencies[curr_word] += 1
        else:
            word_frequencies[curr_word] = 1
    return max(word_frequencies, key=word_frequencies.get)