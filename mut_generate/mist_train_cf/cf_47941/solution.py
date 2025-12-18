"""
QUESTION:
Given an array of strings `words` representing an English Dictionary and a lowercase English letter `c`, return the longest word in `words` that can be built one character at a time by other words in `words` and contains `c`. If there are multiple possible answers, return the longest word with the smallest lexicographical order. If there is no answer, return an empty string. 

The function should be named `longestWord` and take two parameters: `words` and `c`. The constraints are `1 <= words.length <= 1000`, `1 <= words[i].length <= 30`, `words[i]` consists of lowercase English letters, and `c` is a lowercase English letter.
"""

def longestWord(words, c):
    # sort the words in reverse order based on length and lexicographical order
    words.sort(key = lambda x: (-len(x), x))
    good_words = set([''])
    for word in words:
        if word[:-1] in good_words and c in word:
            good_words.add(word)
    # since the words are sorted, the first good word found is the longest
    for word in words:
        if word in good_words:
            return word
    return ''