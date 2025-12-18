"""
QUESTION:
Write a function `max_vowels(word_list)` that accepts a list of distinct English words and returns the word or words with the maximum quantity of vowel characters (a, e, i, o, u). If multiple words have the same maximum quantity of vowels, return a list of all such words. Do not use built-in Python functions or third-party libraries.
"""

def entance(word_list):

    if not word_list:
        return None

    vowels = 'aeiou'
    vowel_count = {}
    max_count = 0

    for word in word_list:
        count = 0
        for char in word:
            if char in vowels:
                count += 1
        if count > max_count:
            max_count = count
        if count in vowel_count.keys():
            vowel_count[count].append(word)
        else:
            vowel_count[count] = [word]

    return vowel_count[max_count]