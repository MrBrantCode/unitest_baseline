"""
QUESTION:
Implement the `convert_to_pig_latin(string: str) -> str` function. The function takes a string consisting of only alphabetic characters as input and returns the transformed string in Pig Latin. The transformation rules are as follows:

- If the word starts with a vowel (a, e, i, o, u), add "ay" to the end of the word.
- If the word starts with a consonant, move the consonant cluster to the end of the word, and add "ay" to the end.
- Maintain the original capitalization of the word.

For example, "Hello" should be transformed into "Ellohay", "Apple" into "Appleay", and "Hello World" into "Ellohay Orldway".
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