"""
QUESTION:
Create a function named `cap_vow_con` that takes a lowercase string sentence as input. The function should return three values: the input sentence with the first letter of each word capitalized, the count of vowels, and the count of consonants in the sentence. Only consider English alphabets for counting vowels and consonants.
"""

def cap_vow_con(sentence):
    vowels = 'aeiou'
    sentence = sentence.lower() # normalize the sentence to lowercase
    count_vowels = sum(1 for char in sentence if char in vowels)
    count_consonants = sum(1 for char in sentence if char.isalpha() and char not in vowels)
    sentence_cap = sentence.title() # capitalize the first letter of each word
    return sentence_cap, count_vowels, count_consonants