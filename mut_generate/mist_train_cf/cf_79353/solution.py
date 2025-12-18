"""
QUESTION:
Write a function `count_consonants` that takes a list of sentences as input and returns the total count of consonants in the remaining sentences after applying the following rules:
- Remove sentences with less than 5 words.
- Remove sentences that start with a vowel or end with a non-consonant.
- Remove sentences containing any word that is a palindrome or contains more than 2 vowels.
- Remove sentences containing any pair of anagrams.
The function should ignore non-alphabetic characters and consider only alphabets in lowercase.
"""

import re

def count_consonants(sentences):
    total_consonants = 0
    consonants = 'bcdfghjklmnpqrstvwxyz'
    vowels = 'aeiou'
    to_be_removed = set()

    # Identify sentences to be removed
    for sentence in sentences:
        words = sentence.lower().split()
        if len(words)<5 or words[0][0] in vowels or words[-1][-1] not in consonants: 
            to_be_removed.add(sentence)
        else:
            for word in words:
                clean_word = re.sub(r'\W', '', word)
                if clean_word == clean_word[::-1] or sum(clean_word.count(vowel) for vowel in vowels)>2:
                    to_be_removed.add(sentence)
                    break
    
    # Checking for anagrams
    for i in range(len(sentences)):
        if sentences[i] not in to_be_removed:
            for j in range(i+1, len(sentences)):
                if sentences[j] not in to_be_removed:
                    words1 = [re.sub(r'\W', '', word).lower() for word in sentences[i].split()]
                    words2 = [re.sub(r'\W', '', word).lower() for word in sentences[j].split()]
                    for word1 in words1:
                        for word2 in words2:
                            if word1 != word2 and sorted(word1) == sorted(word2):
                                to_be_removed.add(sentences[i])
                                to_be_removed.add(sentences[j])
                                break

    # Removing unwanted sentences
    for sentence in list(to_be_removed):
        if sentence in sentences:
            sentences.remove(sentence)

    # Now all the remaining sentences should qualify for the actual count:
    for sentence in sentences:
        words = re.sub(r'\W', ' ', sentence).lower().split()
        for word in words:
            for char in word:
                if char in consonants:
                    total_consonants += 1
    return total_consonants