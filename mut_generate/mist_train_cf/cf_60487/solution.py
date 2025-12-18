"""
QUESTION:
Write a function named `count_consonants` that takes a list of sentences as input and returns the total count of consonants from the sentences. The function should disregard any sentences that start with a vowel, end with a consonant, contain numbers, special characters, or are less than 5 words in length. It should also disregard sentences that contain words that are palindromes, anagrams of each other, or have more than 3 vowels. The function should handle sentences with mixed case letters.
"""

import re

def count_consonants(sentences):
    total_consonants = 0
    consonants = 'bcdfghjklmnpqrstvwxyz'
    vowels = 'aeiou'
    to_be_removed = []
    
    # Identify sentences to be removed
    for sentence in sentences:
        words = sentence.lower().split()
        if len(words)<5 or words[0][0] in vowels or words[-1][-1] in consonants: 
            to_be_removed.append(sentence)
        else:
            for word in words:
                if (word==word[::-1]) or (sum(word.count(vowel) for vowel in vowels)>3 ):
                    to_be_removed.append(sentence)
                    break
                # Checking for anagrams
                for second_word in words:
                    if words!=second_word and sorted(word)==sorted(second_word):
                        to_be_removed.append(sentence)
                        break
                        
    #Removing unwanted sentences
    for sentence in to_be_removed:
        if sentence in sentences:
            sentences.remove(sentence)
    
    # Now all the remaining sentences should qualify for the actual count:
    for sentence in sentences:
        words = re.sub(r'\W+', ' ', sentence).lower().split()
        for word in words:
            for char in word:
                if char in consonants:
                    total_consonants += 1
    return total_consonants