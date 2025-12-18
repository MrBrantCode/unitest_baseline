"""
QUESTION:
Implement the function `count_unique_vowels(sentence)` that counts the number of unique vowels in a sentence, considering only vowels that occur after a consonant and before another consonant, and ignoring any vowels that occur at the beginning or end of a word. The solution should have a time complexity of O(n) and a space complexity of O(1), where n is the length of the sentence.
"""

def count_unique_vowels(sentence):
    vowels = set(['a', 'e', 'i', 'o', 'u'])
    consonants = set(['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z'])
    unique_vowels = set()
    prev_char = ''
    
    for char in sentence:
        if char.lower() in vowels and prev_char.lower() in consonants:
            unique_vowels.add(char.lower())
        prev_char = char
    
    return len(unique_vowels)