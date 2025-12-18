"""
QUESTION:
Create a function named `calculate_vowels` that takes a sentence as input and returns a dictionary where the keys are the individual words of the sentence and the values are a dictionary with vowel counts (a, e, i, o, u) for each word. The function should ignore case sensitivity and include words with punctuation. The time complexity of the solution should be as efficient as possible, aiming for linear time complexity.
"""

def calculate_vowels(sentence):
    vowels = "aeiou"
    words_dict = {}
    words = sentence.split()
    
    for word in words:
        word_lowered = word.lower()  
        vowels_dict = {vowel: word_lowered.count(vowel) for vowel in vowels}
        words_dict[word] = vowels_dict

    return words_dict