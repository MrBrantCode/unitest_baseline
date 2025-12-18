"""
QUESTION:
Write a Python function `convert_to_pig_latin` that takes a string of English text as input, removes all punctuation, and converts each word to Pig Latin. Pig Latin is a coded language where the first letter of each word is moved to the end of the word and "ay" is appended, unless the word starts with a vowel, in which case "ay" is simply appended to the end of the word. The function should return the resulting Pig Latin text as a string.
"""

import string

def convert_to_pig_latin(text):
    # eliminate punctuations
    text = text.translate(str.maketrans('', '', string.punctuation))
    
    # split the text into words
    words = text.split()
    
    # convert each word to pig latin
    pig_latin_words = []
    for word in words:
        # check if the first letter is a vowel
        if word[0].lower() in 'aeiou':
            pig_latin_words.append(f'{word}ay')
        else:
            # move the first letter to the end and append 'ay'
            pig_latin_words.append(f'{word[1:]}{word[0]}ay')
    
    # combine the pig latin words into a sentence
    pig_latin_text = ' '.join(pig_latin_words)
    
    return pig_latin_text