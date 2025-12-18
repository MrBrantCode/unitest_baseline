"""
QUESTION:
Write a function `findLongestWord(s, dictionary)` that returns the longest string in the dictionary that can be formed by deleting some of the given string `s` characters. If there is more than one possible result, return the longest word with the smallest lexicographical order. The returned word must not contain any consecutive repeating characters. The function should take two parameters: `s`, a string of length between 1 and 1000 consisting of lowercase English letters, and `dictionary`, a list of strings each of length between 1 and 1000 consisting of lowercase English letters.
"""

def findLongestWord(s, dictionary):
    def valid(str):
        it = iter(s)
        return all(c in it for c in str)
        
    res = ""
    for word in dictionary:
        if valid(word):
            if len(word) > len(res) or len(word) == len(res) and word < res:
                res = word
    return res