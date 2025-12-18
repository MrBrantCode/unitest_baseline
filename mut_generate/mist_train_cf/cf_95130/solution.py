"""
QUESTION:
Write a function `count_words(sentence: str) -> Dict[str, int]` that returns a dictionary containing the count of each word in the given sentence, excluding common words such as "the", "a", "an", etc.

The input sentence will only contain alphabets and spaces, will not be empty, and will not have leading or trailing spaces. All words will be separated by a single space. The function should perform case-insensitive counting.
"""

from typing import Dict

def count_words(sentence: str) -> Dict[str, int]:
    common_words = set(["the", "a", "an", "and", "or", "but", "if", "is", "are", "was", "were", "has", "have", "had", "do", "does", "did", "for", "of", "with", "at", "by", "from", "in", "out", "on", "off", "to", "into", "onto", "up", "down", "over", "under", "through", "between", "among", "after", "before", "underneath", "above", "below", "around", "about", "near", "far", "away", "beneath", "beside", "besides", "behind", "ahead", "along", "upon", "against", "throughout", "during", "within", "without", "toward", "towards", "onto", "into", "over", "through", "behind", "in", "out", "up", "down", "on", "off", "across", "about", "above", "after", "against", "along", "among", "around", "as", "at", "before", "behind", "below", "beneath", "beside", "between", "beyond", "but", "by", "despite", "during", "for", "from", "in", "inside", "into", "near", "of", "off", "on", "onto", "out", "outside", "over", "past", "regarding", "round", "since", "through", "throughout", "till", "to", "toward", "under", "underneath", "until", "unto", "up", "upon", "with", "within", "without"])
    word_count = {}
    
    words = sentence.split()
    for word in words:
        word = word.lower()
        if word not in common_words:
            if word in word_count:
                word_count[word] += 1
            else:
                word_count[word] = 1
    
    return word_count