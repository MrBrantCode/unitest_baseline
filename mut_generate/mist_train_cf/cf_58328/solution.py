"""
QUESTION:
Design a function `pig_latin_translator` that takes a string of English question sentence as input and returns its Pig Latin version. The Pig Latin transformation rule is to move the first consonant or consonant cluster of a word to the end followed by "ay" if the word starts with a consonant, and add "way" at the end if the word starts with a vowel. The function should handle each word in the sentence separately and return the transformed sentence with a question mark at the end. The input string only contains lowercase letters and spaces, and does not contain punctuation other than a question mark at the end.
"""

def pig_latin_translator(english_question):
    words = english_question.split(" ") 
    pig_latin_list = [] 
    for word in words:
        if word[0] in 'aeiou': 
            pig_latin_word = word + 'way' 
        else: 
            pig_latin_word = word[1:] + word[0] + 'ay' 
        pig_latin_list.append(pig_latin_word)
    pig_latin_question = ' '.join(pig_latin_list)
    return pig_latin_question + '?'     