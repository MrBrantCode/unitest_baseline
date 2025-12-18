"""
QUESTION:
Write a function `sort_by_second_syllable_length(words)` that takes a list of words as input and returns the list sorted by the length of the second syllable in each word. A syllable is defined as a vowel sound, and a group of sequential vowels is considered one syllable. If a word has no second syllable, consider its second syllable length as 0. The function should be case-insensitive and ignore punctuation marks at the end of the words.
"""

def count_syllable_len(word):
    vowels = 'aeiou' 
    word = word.lower().strip(".:;?!")
    count = 0 
    word_syllable_lengths = []

    # Count syllable lengths
    for letter in word:
        if letter in vowels:
            count +=1
        else:
            if count > 0:
                word_syllable_lengths.append(count)
                count = 0

    # Add last syllable length
    if count > 0:
        word_syllable_lengths.append(count)

    # If word has second syllable return its length else return 0 
    if len(word_syllable_lengths) >= 2:
        return word_syllable_lengths[1]
    else:
        return 0

def sort_by_second_syllable_length(words):
    return sorted(words, key=count_syllable_len)