"""
QUESTION:
Design a function called `reverse_words_vowel_count` that takes a sentence as input. The function should reverse each word in the sentence while maintaining their original sequence, ignore non-alphabetical characters, and count the number of vowels in the reversed words. The function should return the modified sentence with reversed words and the total vowel count.
"""

def reverse_words_vowel_count(input_sentence):
    """
    This function takes a sentence as input, reverses each word while maintaining their original sequence, 
    ignores non-alphabetical characters, and counts the number of vowels in the reversed words.
    
    Args:
        input_sentence (str): The input sentence to be processed.

    Returns:
        tuple: A tuple containing the modified sentence with reversed words and the total vowel count.
    """
    # Replace non-word characters with spaces
    sanitized_sentence = ''.join(ch if ch.isalpha() or ch.isspace() else ' ' for ch in input_sentence)

    # Split sentence into list of words
    words = sanitized_sentence.split()

    # Reverse each word
    reversed_words = [word[::-1] for word in words]

    # Join reversed words back into a sentence
    reversed_sentence = ' '.join(reversed_words)

    # Find vowel count in reversed words
    vowel_count = sum(1 for char in reversed_sentence.lower() if char in 'aeiou')

    return reversed_sentence, vowel_count