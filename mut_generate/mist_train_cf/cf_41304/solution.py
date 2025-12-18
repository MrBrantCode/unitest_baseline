"""
QUESTION:
Implement the `searchWordIndex` function that takes a sentence and a search word as input and returns the index of the first occurrence of the search word in the sentence. The function should use the Knuth-Morris-Pratt (KMP) algorithm. If the sentence starts with the search word, return 0. If the search word is found, return its index. If not found, return -1. The input parameters are `sentence` and `searchWord`, both strings, and the return value is an integer representing the index of the search word.
"""

def searchWordIndex(sentence: str, searchWord: str) -> int:
    if sentence.startswith(searchWord):
        return 0
    def computeLPSArray(pattern):
        lps = [0] * len(pattern)
        length = 0
        i = 1
        while i < len(pattern):
            if pattern[i] == pattern[length]:
                length += 1
                lps[i] = length
                i += 1
            else:
                if length != 0:
                    length = lps[length - 1]
                else:
                    lps[i] = 0
                    i += 1
        return lps

    def KMP(text, pattern):
        lps = computeLPSArray(pattern)
        i, j = 0, 0
        while i < len(text):
            if pattern[j] == text[i]:
                i += 1
                j += 1
            if j == len(pattern):
                return i - j
            elif i < len(text) and pattern[j] != text[i]:
                if j != 0:
                    j = lps[j - 1]
                else:
                    i += 1
        return -1
    p = KMP(sentence, ' ' + searchWord)
    if p == -1:
        return -1
    return p - 1