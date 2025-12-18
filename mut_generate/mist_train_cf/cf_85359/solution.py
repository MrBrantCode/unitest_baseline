"""
QUESTION:
Create a function `remove_alphabet_and_count_frequency(text, letter)` that takes a string `text` and a single character `letter` as input. The function should remove all instances of `letter` from `text` (ignoring case) and return the resulting string along with a dictionary containing the frequency count of each remaining letter in the text. The function should handle case insensitivity and not count the frequency of the removed letter.
"""

def remove_alphabet_and_count_frequency(text, letter):
    letter_count = {}
    letter = letter.lower() 
    edited_text = text.lower()
    
    for i in edited_text:
        if i != letter:
            if i in letter_count:
                letter_count[i] += 1
            else:
                letter_count[i] = 1
    
    edited_text = edited_text.replace(letter, '')
    
    return edited_text, letter_count