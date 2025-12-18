"""
QUESTION:
Create a function `count_vowels` that takes a sentence as input and returns the number of vowels that occur in the sentence, while ignoring any vowels that occur within a word that starts with a consonant. Assume the input sentence only contains alphabets and spaces, and consider 'a', 'e', 'i', 'o', 'u' as vowels.
"""

def count_vowels(sentence):
    vowels = ['a', 'e', 'i', 'o', 'u']
    count = 0
    words = sentence.split()

    for word in words:
        if word[0].lower() not in vowels:  # Ignore words starting with a consonant
            continue
        for char in word:
            if char.lower() in vowels:
                count += 1

    return count