"""
QUESTION:
Implement a function `pig_latin_converter` that takes a string sentence as input and returns its Pig Latin equivalent. The function should follow these rules:

- If a word starts with a consonant cluster, move the entire cluster to the end of the word and add "ay".
- If a word starts with a vowel or a vowel cluster, add "way" at the end.
- If a word starts with a capitalized consonant cluster, the converted word should also be capitalized.
"""

def pig_latin_converter(sentence):
    vowels = "aeiou"
    consonants = "bcdfghjklmnpqrstvwxyz"
    words = sentence.split()
    pig_latin_words = []

    for word in words:
        if word[0].lower() in vowels:
            pig_latin_word = word + "way"
        else:
            cluster = ""
            i = 0
            while i < len(word) and word[i].lower() in consonants:
                cluster += word[i]
                i += 1
            pig_latin_word = word[i:] + cluster + "ay"
            
        if word[0].isupper():
            pig_latin_word = pig_latin_word.capitalize()
            
        pig_latin_words.append(pig_latin_word)
    
    return " ".join(pig_latin_words)