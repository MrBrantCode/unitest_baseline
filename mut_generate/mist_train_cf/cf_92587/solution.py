"""
QUESTION:
Write a function `convert_to_pig_latin(string: str) -> str` that takes a string of alphabetic characters as input and returns the transformed string in Pig Latin. The function should maintain the original capitalization of the words and apply the following rules: 
- If a word starts with a vowel, add "ay" to the end.
- If a word starts with a consonant, move the consonant cluster to the end and add "ay".
"""

def convert_to_pig_latin(string: str) -> str:
    # Split the string into individual words
    words = string.split()

    transformed_words = []
    for word in words:
        # Check if the word starts with a vowel
        if word[0].lower() in ['a', 'e', 'i', 'o', 'u']:
            transformed_word = word + 'ay'
        else:
            # Find the index of the first vowel
            vowel_index = next((i for i, c in enumerate(word) if c.lower() in ['a', 'e', 'i', 'o', 'u']), None)
            # Move the consonant cluster to the end of the word
            transformed_word = word[vowel_index:] + word[:vowel_index] + 'ay'

        # Maintain the original capitalization of the word
        if word[0].isupper():
            transformed_word = transformed_word.capitalize()

        transformed_words.append(transformed_word)

    # Join all the transformed words back together
    transformed_string = ' '.join(transformed_words)
    return transformed_string