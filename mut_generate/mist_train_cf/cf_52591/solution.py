"""
QUESTION:
Write a function named `pig_latin_translator` that takes a string `input_string` as input, removes all punctuation from the string, and translates it into Pig Latin. The translation rule is as follows: if the word starts with a vowel, append "way" to the end; otherwise, move the first letter to the end and append "ay". Return the translated string.
"""

import string

def pig_latin_translator(input_string):
    # Remove punctuation
    punctuations = string.punctuation
    input_string = ''.join(ch for ch in input_string if ch not in punctuations)

    # Convert to Pig Latin
    words = input_string.split()
    latin_words = []
    for word in words:
        # If the word starts with a vowel, simply append "way" to the end of the word
        if word[0].lower() in 'aeiou':
            latin_words.append(word + 'way')
        else:
            # If the word does not start with a vowel, 
            # then the first letter is moved to the end of the word and "ay" is added to it
            latin_words.append(word[1:] + word[0] + 'ay')

    return ' '.join(latin_words)