"""
QUESTION:
Write a function called `reverse_words` that takes a string of words as input, reverses their order, and returns two strings. The first string should contain the words in reverse order, and the second string should contain the words in reverse order with all vowels removed. Do not use any built-in reverse functions.
"""

def reverse_words(text):
    words = text.split(' ')
    reversed_words = ''
    reversed_no_vowels = ''

    for i in range(len(words)-1, -1, -1):
        reversed_words += words[i] + ' '

        word_no_vowel = ''
        for letter in words[i]:
            if letter.lower() not in 'aeiou':
                word_no_vowel += letter
        reversed_no_vowels += word_no_vowel + ' '

    return reversed_words.strip(), reversed_no_vowels.strip()