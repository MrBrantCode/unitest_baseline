"""
QUESTION:
Create a function named `select_phrases(s, n, m)` that takes a string `s` and two natural numbers `n` and `m` as inputs. The function should return a list of phrases from `s`, where each phrase is a collection of words separated by a space with exactly `n` consonants and `m` vowels. If two identical phrases appear sequentially in `s`, merge them into one and remove one random consonant and one random vowel from the merged phrase. If `s` is empty, return an empty list.
"""

def select_phrases(s, n, m):
    # Define vowels and consonants
    vowels = "aeiou"
    consonants = "bcdfghjklmnpqrstvwxyz"
    
    phrases = []
    words = s.split(" ")
    temp_phrase = ""

    for word in words:
        nc = sum(c in consonants for c in word.lower()) # Number of consonants in the word
        nv = sum(v in vowels for v in word.lower()) # Number of vowels in the word
        if (nc == n) and (nv == m):
            if (temp_phrase == word):
                if nc > 0 and nv > 0: # Check for vowels and consonants
                    # remove one random consonant and one random vowel from the word
                    for char in word.lower():
                        if char in vowels and nv > 0:
                            word = word.replace(char, '', 1)
                            nv -= 1
                        if char in consonants and nc > 0:
                            word = word.replace(char, '', 1)
                            nc -= 1
            temp_phrase = word
            phrases.append(temp_phrase) # Append word to phrases list

    return phrases