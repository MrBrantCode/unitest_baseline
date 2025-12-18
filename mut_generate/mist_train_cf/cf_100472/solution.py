"""
QUESTION:
Write a function `find_words_with_three_vowels` that takes a list of words as input and returns a list of words that contain exactly three vowels. The vowels in these words must appear in alphabetical order.
"""

def find_words_with_three_vowels(words):
    result = []
    vowels = 'aeiou'
    for word in words:
        vowel_count = 0
        vowel_order = ''
        for letter in word:
            if letter in vowels:
                vowel_count += 1
                vowel_order += letter
        if vowel_count == 3 and vowel_order == ''.join(sorted(vowel_order)):
            result.append(word)
    return result