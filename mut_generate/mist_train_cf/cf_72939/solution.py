"""
QUESTION:
Write a function called `pig_latin(word)` that translates a string into Pig Latin. The function should handle words that start with a vowel by appending "way" to the end of the word, and words that start with a consonant by moving the first letter to the end of the word and appending "ay". The function should also preserve any punctuation at the end of the word and maintain the original casing of the word. If the input string contains multiple words, the function should translate each word separately. If the input is not a non-empty string, the function should return an error message.
"""

def pig_latin(word):
    if not isinstance(word, str) or word.strip() == '':
        return 'Invalid input. Please enter a non-empty string.'   

    vowels = ['a', 'e', 'i', 'o', 'u']
    translated_words = []
    punctuation = ''

    words = word.split()
    for word in words:
        if not word[-1].isalpha():
            punctuation = word[-1]
            word = word[:-1]

        first_letter = word[0]
        if first_letter.lower() in vowels:
            translated_word = word + "way" + punctuation
        else:
            remaining_letters = word[1:]
            translated_word = remaining_letters + first_letter + "ay" + punctuation

        if word[0].isupper():
            translated_word = translated_word.capitalize()
        translated_words.append(translated_word)

    return ' '.join(translated_words)