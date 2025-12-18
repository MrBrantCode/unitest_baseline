"""
QUESTION:
Write a function `count_unique_vowels(sentence)` that counts the number of unique vowels in a sentence, considering only vowels that occur after a consonant and before another consonant, excluding vowels at the beginning or end of a word. The function should have a time complexity of O(n), where n is the length of the sentence, and a space complexity of O(1).
"""

def count_unique_vowels(sentence):
    vowels = set('aeiou')
    unique_vowels = set()
    prev_consonant = False

    for i in range(1, len(sentence)-1):
        if sentence[i] in vowels:
            if prev_consonant and (i == len(sentence) - 2 or sentence[i+1] not in vowels):
                unique_vowels.add(sentence[i])
            prev_consonant = False
        elif sentence[i] not in vowels and (i == 0 or sentence[i-1] not in vowels) and (i < len(sentence) - 1 and sentence[i+1] in vowels):
            prev_consonant = True

    return len(unique_vowels)