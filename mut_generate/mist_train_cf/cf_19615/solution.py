"""
QUESTION:
Write a function `count_words_with_ed` that takes a string `text` as input. Return the count of words in the text that contain the string "ed" and start with a vowel (either lowercase or uppercase).
"""

def count_words_with_ed(text):
    vowels = ['a', 'e', 'i', 'o', 'u']
    words = text.split()
    count = 0
    for word in words:
        if 'ed' in word and word[0].lower() in vowels:
            count += 1
    return count