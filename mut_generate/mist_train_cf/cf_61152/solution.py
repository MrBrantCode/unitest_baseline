"""
QUESTION:
Develop a function named `char_frequency` that takes a sentence as input and returns a dictionary where each key is a unique character in the sentence and each value is the respective character's frequency. The function should ignore spaces and punctuation, and consider uppercase and lowercase characters as the same. The input sentence may contain letters, spaces, and punctuation.
"""

def char_frequency(sentence):
    sentence = sentence.lower() 
    frequency = {} 

    for char in sentence:
        if char.isalpha(): 
            if char not in frequency:
                frequency[char] = 1
            else:
                frequency[char] += 1

    return frequency