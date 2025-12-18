"""
QUESTION:
Write a function `find_word_max_vowels(words)` that takes a list of unique English words and returns the word with the maximum number of vowel characters. In case of a tie, the function should prefer words with more repeated characters.
"""

def find_word_max_vowels(words):
    def count_vowels(word):
        vowel_count = 0
        repeat_count = 0
        char_count = {}
        for char in word:
            if char.lower() in 'aeiou':
                vowel_count += 1
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1
        repeat_count = sum([c-1 for c in char_count.values() if c > 1])
        return vowel_count, repeat_count
    
    max_vowel_count = 0
    max_repeat_count = 0
    word_max_vowels = ''
    
    for word in words:
        vowel_count, repeat_count = count_vowels(word)
        if vowel_count > max_vowel_count or \
           (vowel_count == max_vowel_count and repeat_count > max_repeat_count):
            max_vowel_count = vowel_count
            max_repeat_count = repeat_count
            word_max_vowels = word
            
    return word_max_vowels