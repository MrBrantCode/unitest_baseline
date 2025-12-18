"""
QUESTION:
Create a function `advanced_ordered_list(word_list, ascending=False, min_length=0)` that accepts a list of words and two optional parameters: `ascending` (default is `False`) to control the direction of the sort, and `min_length` (default is `0`) to filter out words with a length less than the minimum length. 

The function should return a list of anagrams from the original list, sorted in the specified order. The casing of the words is irrelevant and the function should be able to handle duplicate words.
"""

def advanced_ordered_list(word_list, ascending=False, min_length=0):
    if not word_list:
        return []

    word_list = [''.join(sorted(word.lower())) for word in word_list if len(word) >= min_length]

    anagram_dict = {}
    for word in word_list:
        if word in anagram_dict:
            anagram_dict[word] += 1
        else:
            anagram_dict[word] = 1

    word_list = [word for word, count in anagram_dict.items() if count > 1]

    word_list.sort(reverse=not ascending)

    return [''.join(sorted(word)) for word in word_list]