"""
QUESTION:
Write a function named `pig_latin_converter` that takes a string sentence as input and returns its Pig Latin translation. 

The function should handle the following rules: 
- If a word starts with a vowel, add "way" to the end of the word.
- If a word starts with a consonant or a consonant cluster, move the consonant or consonant cluster to the end of the word and add "ay".
- If a word ends with a punctuation mark, move the punctuation mark to the end of the Pig Latin word.
- The function should maintain the original capitalization of the input sentence.
"""

def pig_latin_converter(sentence):
    """
    Translate a given English sentence into Pig Latin.
    
    Parameters:
    sentence (str): The input sentence to be translated.
    
    Returns:
    str: The Pig Latin translation of the input sentence.
    """
    words = sentence.split()
    pig_latin_words = []
    
    for word in words:
        punctuation = ""
        if word[-1] in [".", ",", "?", "!"]:
            punctuation = word[-1]
            word = word[:-1]
        
        if word[0].isupper():
            is_upper = True
            word = word.lower()
        else:
            is_upper = False
        
        if word[0] in "aeiou":
            pig_latin_word = word + "way"
        else:
            vowel_index = 0
            while vowel_index < len(word) and word[vowel_index] not in "aeiou":
                vowel_index += 1
            pig_latin_word = word[vowel_index:] + word[:vowel_index] + "ay"
        
        if is_upper:
            pig_latin_word = pig_latin_word.capitalize()
        
        pig_latin_word += punctuation
        pig_latin_words.append(pig_latin_word)
    
    return " ".join(pig_latin_words)