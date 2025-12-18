"""
QUESTION:
Convert a sentence to Pig Latin using the `convert_to_pig_latin` function. The function should take a string sentence as input and return the transformed sentence in Pig Latin. The rules for transformation are as follows:

- If a word starts with a vowel, add "ay" to the end of the word.
- If a word starts with a consonant, move the consonant cluster to the end of the word and add "ay".
- Maintain the original capitalization of the words.
- If a word ends with punctuation marks (., !, ?), move the punctuation marks to the end of the transformed word.

Restrictions: The input sentence contains only alphabetic characters and punctuation marks.
"""

def convert_to_pig_latin(sentence: str) -> str:
    vowels = {'a', 'e', 'i', 'o', 'u'}
    punctuation_marks = {'.', '!', '?'}
    words = sentence.split()
    transformed_words = []
    
    for word in words:
        if word[-1] in punctuation_marks:
            punctuation = word[-1]
            word = word[:-1]
        else:
            punctuation = ''
            
        if word[0].lower() in vowels:
            transformed_word = word + 'ay'
        else:
            vowel_index = 0
            for i, char in enumerate(word):
                if char.lower() in vowels:
                    vowel_index = i
                    break
            
            consonant_cluster = word[:vowel_index]
            transformed_word = word[vowel_index:] + consonant_cluster + 'ay'
        
        transformed_word += punctuation
        
        transformed_words.append(transformed_word)
    
    return ' '.join(transformed_words)