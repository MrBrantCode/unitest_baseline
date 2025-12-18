"""
QUESTION:
Write a function named `word_count` that takes two strings `str1` and `str2` as input and returns three values: the number of unique words in `str1`, the number of unique words in `str2`, and the number of common words appearing in both strings. The word comparison should be case-insensitive and punctuation should not be accounted for in words.
"""

def word_count(str1, str2):
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    str1_no_punct = ""
    str2_no_punct = ""
    for char in str1:
        if char not in punctuations:
            str1_no_punct = str1_no_punct + char
    for char in str2:
        if char not in punctuations:
            str2_no_punct = str2_no_punct + char

    str1_words = set(word.lower() for word in str1_no_punct.split())
    str2_words = set(word.lower() for word in str2_no_punct.split())
    
    common_words = str1_words & str2_words  
    unique_words_count_str1 = len(str1_words)
    unique_words_count_str2 = len(str2_words)
    common_words_count = len(common_words)

    return unique_words_count_str1, unique_words_count_str2, common_words_count