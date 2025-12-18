"""
QUESTION:
Create a Python function named `vowel_count` that takes a list of words as input and returns a list of words with the highest number of vowels, considering 'y' as a vowel and being case-insensitive. If multiple words have the same maximum number of vowels, return all such words. If the input list is empty, return 'The list is empty.'
"""

def vowel_count(word_list):
    """
    Returns a list of words with the highest number of vowels from the input list.
    
    Args:
        word_list (list): A list of words.
    
    Returns:
        list: A list of words with the highest number of vowels. If the input list is empty, returns 'The list is empty.'
    """
    
    if len(word_list) == 0:
        return 'The list is empty.'

    vowels = 'aeiouyAEIOUY'
    max_vowel_word = {}
    max_vowel_count = 0

    for word in word_list:
        count = sum(1 for char in word if char in vowels)
        if count > max_vowel_count:
            max_vowel_count = count
            max_vowel_word = {word: max_vowel_count}
        elif count == max_vowel_count:
            max_vowel_word[word] = max_vowel_count

    return [word for word, count in max_vowel_word.items() if count == max_vowel_count]