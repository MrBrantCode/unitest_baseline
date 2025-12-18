"""
QUESTION:
Create a function `common_words(str1, str2, str3)` that takes three strings as input and returns a set of unique common words that appear in all three strings while ignoring case sensitivity and punctuation marks at the beginning or end of words, along with the count of unique common words.
"""

def common_words(str1, str2, str3):
    str1_words = set(word.strip('.,!?;:\'\"').lower() for word in str1.split())
    str2_words = set(word.strip('.,!?;:\'\"').lower() for word in str2.split())
    str3_words = set(word.strip('.,!?;:\'\"').lower() for word in str3.split())
    common = str1_words & str2_words & str3_words
    return common, len(common)