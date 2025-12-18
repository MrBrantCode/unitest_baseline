"""
QUESTION:
Write a function named `word_character_stats` that takes a string of text as input. The function should return a dictionary where the keys are unique words in the text and the values are dictionaries containing the following information: the word's frequency in the text, the number of characters in the word, the number of vowels in the word, the number of consonants in the word, and the number of special characters in the word. The function should ignore case sensitivity when counting word frequencies, and it should not include punctuation marks as part of the words.
"""

import re

def word_character_stats(text):
    
    vowels = 'aeiou'
    text = text.lower()
    words = re.findall(r'\b\w+\b', text)
    
    word_counts = dict()
    full_stats = dict()
    
    for word in words:
        word_counts[word] = words.count(word)
        
        char_count = len(word)
        vowel_count = sum(word.count(ch) for ch in vowels)
        consonant_count = char_count - vowel_count
        special_count = len(re.findall("[@_!#$%^&*()<>?/\|}{~:]", word))

        full_stats[word] = {
            'word_count': word_counts[word],
            'char_count': char_count,
            'vowel_count': vowel_count,
            'consonant_count': consonant_count,
            'special_count': special_count
        }
        
    return full_stats