"""
QUESTION:
Write a function to count the number of vowels in a given sentence. The function should take a string as input and return the total number of vowels (both lowercase and uppercase) in the sentence. The vowels to be considered are 'a', 'e', 'i', 'o', and 'u'.
"""

def count_vowels(sentence):
    """
    This function takes a string as input and returns the total number of vowels (both lowercase and uppercase) in the sentence.

    Args:
        sentence (str): The input sentence.

    Returns:
        int: The total number of vowels in the sentence.
    """
    num_vowels = 0
    for char in sentence:
        if char.lower() in "aeiou":
            num_vowels += 1
    return num_vowels