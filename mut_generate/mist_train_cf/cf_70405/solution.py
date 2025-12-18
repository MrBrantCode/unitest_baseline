"""
QUESTION:
Create a function `getClosestVowel(word)` that takes a single word as input. The function should find the nearest vowel that is surrounded by two consonants, starting from the end of the word. Vowels at the start or end of the word should be ignored. If no such vowel is found, the function should return an empty string. The input word is guaranteed to only contain English alphabets.
"""

def getClosestVowel(word):
    vowels = 'AEIOUaeiou'
    word = word[1:-1]  # Ignore first and last characters
    for i in range(len(word)-1, -1, -1):  # Loop backwards
        if word[i] in vowels:
            if i>0 and word[i-1] not in vowels and i<len(word)-1 and word[i+1] not in vowels:
                return word[i]
    return ''