"""
QUESTION:
Write a function `findLongestWord(s, dictionary)` that takes a string `s` and a list of strings `dictionary` as input. The function should return the longest string in the dictionary that can be formed by deleting some characters from `s`, without containing any consecutive repeating characters. If there are multiple possible results, return the longest word with the smallest lexicographical order. If no such word exists, return an empty string. The length of `s` and each string in `dictionary` is between 1 and 1000, and they consist of lowercase English letters.
"""

def findLongestWord(s, dictionary):
    def is_subsequence(s, t):
        iter_t = iter(t)
        return all(c in iter_t for c in s)
    
    def no_consecutive_chars(s):
        for i in range(len(s)-1):
            if s[i] == s[i+1]:
                return False
        return True

    dictionary.sort(key=lambda x: (-len(x), x))  
    for word in dictionary:
        if is_subsequence(word, s) and no_consecutive_chars(word):
            return word
    return ""