"""
QUESTION:
Pig Latin is an English language game where the goal is to hide the meaning of a word from people not aware of the rules.

So, the goal of this kata is to wite a function that encodes a single word string to pig latin.

The rules themselves are rather easy:

1) The word starts with a vowel(a,e,i,o,u) -> return the original string plus "way".

2) The word starts with a consonant -> move consonants from the beginning of the word to the end of the word until the first vowel, then return it plus "ay".

3) The result must be lowercase, regardless of the case of the input. If the input string has any non-alpha characters, the function must return None, null, Nothing (depending on the language).

4) The function must also handle simple random strings and not just English words.

5) The input string has no vowels -> return the original string plus "ay".

For example, the word "spaghetti" becomes "aghettispay" because the first two letters ("sp") are consonants, so they are moved to the end of the string and "ay" is appended.
"""

def encode_to_pig_latin(word: str) -> str:
    VOWELS = set('aeiou')
    
    # Convert the word to lowercase
    lower_word = word.lower()
    
    # Check if the word contains only alphabetic characters
    if not lower_word.isalpha():
        return None
    
    # Check if the word contains any vowels
    if set(lower_word) & VOWELS:
        # If the word starts with a vowel
        if lower_word[0] in VOWELS:
            return lower_word + 'way'
        else:
            # Move consonants from the beginning to the end until the first vowel
            while lower_word[0] not in VOWELS:
                lower_word = lower_word[1:] + lower_word[0]
            return lower_word + 'ay'
    else:
        # If the word has no vowels
        return lower_word + 'ay'