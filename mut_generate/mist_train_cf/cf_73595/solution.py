"""
QUESTION:
Implement a function `countCharacters(words, chars)` that takes an array of strings `words` and a string `chars` as input. A string is considered good if it can be formed by characters from `chars` in the same order as they appear in `chars` and contains at least one vowel. Return the sum of lengths of all good strings in `words`. The function should handle arrays of strings of length between 1 and 1000 and strings of length between 1 and 100, containing only lowercase English letters.
"""

def countCharacters(words, chars):
    result = 0
    vowels = {'a', 'e', 'i', 'o', 'u'}
    for word in words:
        temp = list(chars)
        isvalid = True
        hasVowel = False
        for letter in word:
            if letter in temp:
                if letter in vowels:
                    hasVowel = True
                temp.remove(letter) # remove letters already used
            else:
                isvalid = False
                break
        if isvalid and hasVowel:
            result += len(word)
    return result