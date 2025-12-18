"""
QUESTION:
Write a function `change_case_and_remove_duplicates` that takes a list of words as input, removes duplicates while preserving the original order, and converts each word to lowercase if it's the first occurrence of that word, or to uppercase if it's the second or subsequent occurrence of that word is not found, but for this case keep it in lowercase. The list can contain words with varying lengths and special characters.
"""

def change_case_and_remove_duplicates(word_list):
    """
    Removes duplicates from a list of words while preserving the original order, 
    and converts each word to lowercase if it's the first occurrence of that word, 
    or keeps it in lowercase if it's the second or subsequent occurrence.

    Args:
        word_list (list): A list of words

    Returns:
        list: A list of words with duplicates removed and case modified
    """
    seen = set()
    processed_words = []
    for word in word_list:
        lowercase_word = word.lower()
        if lowercase_word not in seen:
            seen.add(lowercase_word)
            processed_words.append(lowercase_word)
    return processed_words