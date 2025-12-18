"""
QUESTION:
Write a function named `most_vowels(sentence)` that returns the word with the most vowels in a given sentence. The input sentence is a string of English words, and the function should return a string representing the word with the highest count of vowels (a, e, i, o, u). If there are multiple words with the same highest vowel count, the function can return any of them.
"""

def most_vowels(sentence):
    words = sentence.split(" ")
    highest_count = 0
    most_vowels_word = ""
    for word in words:
        num_vowels = 0
        for c in word:
            if c.lower() in ["a", "e", "i", "o", "u"]:
                num_vowels += 1
        if num_vowels > highest_count:
            highest_count = num_vowels
            most_vowels_word = word
    return most_vowels_word