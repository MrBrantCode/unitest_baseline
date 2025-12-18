"""
QUESTION:
Design a function named `vowel_count` that takes two parameters: a list of words and a list of excluded words. The function should return the total count of uppercase vowels present in the words list, excluding any words that are found in the excluded words list. The function should be case-insensitive when checking for excluded words.
"""

def vowel_count(word_list, excluded_list):
    vowels = set('AEIOU')  
    count = 0

    for word in word_list:
        if word.upper() in (excl_word.upper() for excl_word in excluded_list):
            continue
        count += sum(1 for char in word if char in vowels)

    return count