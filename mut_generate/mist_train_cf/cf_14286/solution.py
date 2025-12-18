"""
QUESTION:
Count the number of words in a given string, excluding any occurrences of the word "test" and its variations, using a for loop. The input string is case-sensitive, and the word "test" and its variations should be ignored regardless of case. Write a function named `count_words_excluding_test` that takes a string as input and returns the word count. The function should not use any external libraries.
"""

def count_words_excluding_test(input_string):
    """
    Count the number of words in a given string, excluding any occurrences of the word "test" and its variations.
    
    Args:
        input_string (str): The input string.
    
    Returns:
        int: The word count excluding variations of "test".
    """
    test_variations = ["test", "testing", "tested"]
    words = input_string.split()
    word_count = 0
    for word in words:
        if word.lower() not in test_variations:
            word_count += 1
    return word_count