"""
QUESTION:
Write a function `convert_to_pig_latin(sentence: str) -> str` that transforms a given sentence into Pig Latin. The rules for the transformation are as follows:

- If a word starts with a vowel (a, e, i, o, u), add "ay" to the end of the word.
- If a word starts with a consonant, move the consonant cluster (all consonants before the first vowel) to the end of the word, and add "ay" to the end.
- Maintain the original capitalization of the words.
- If a word ends with punctuation marks (., !, ?), move the punctuation marks to the end of the transformed word.

The function should take a sentence as input and return the transformed sentence in Pig Latin.
"""

def convert_to_pig_latin(sentence: str) -> str:
    vowels = {'a', 'e', 'i', 'o', 'u'}
    punctuation_marks = {'.', '!', '?'}
    words = sentence.split()
    transformed_words = []
    
    for word in words:
        # Check if the word ends with punctuation marks
        if word[-1] in punctuation_marks:
            # Remove the punctuation marks from the word
            punctuation = word[-1]
            word = word[:-1]
        else:
            punctuation = ''
            
        # Check if the word starts with a vowel
        if word[0].lower() in vowels:
            transformed_word = word + 'ay'
        else:
            # Find the index of the first vowel in the word
            vowel_index = 0
            for i, char in enumerate(word):
                if char.lower() in vowels:
                    vowel_index = i
                    break
            
            # Move the consonant cluster to the end of the word
            consonant_cluster = word[:vowel_index]
            transformed_word = word[vowel_index:] + consonant_cluster + 'ay'
        
        # Add back the punctuation marks if necessary
        transformed_word += punctuation
            
        transformed_words.append(transformed_word)
    
    return ' '.join(transformed_words)