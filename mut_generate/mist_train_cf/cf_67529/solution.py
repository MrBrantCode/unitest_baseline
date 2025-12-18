"""
QUESTION:
You are given a string `s` and a list of strings `words`. All strings in `words` have the same length. Write a function `findSubstring(s, words)` to find all the starting indices of the substrings in `s` that are a concatenation of each word in `words` exactly once, in any order, and without any characters in between. The function should return a list of these indices.

The function has the following constraints:
- The length of `s` is between 1 and 104.
- `s` is composed of lower-case English letters.
- The length of `words` is between 1 and 5000.
- The length of each word in `words` is between 1 and 30.
- Each word in `words` is composed of lower-case English letters.
"""

from collections import Counter

def findSubstring(s, words):
    if not s or not words: 
        return []
    wordBag = Counter(words)   
    wordLen, numWord = len(words[0]), len(words)
    totalLen = wordLen*numWord    
    res = []    

    for i in range(len(s)-totalLen+1):     
        seen = Counter()  
        for j in range(i, i+totalLen, wordLen):  
            currWord = s[j:j+wordLen]  
            if currWord in wordBag:   
                seen[currWord] += 1
                if seen[currWord] > wordBag[currWord]: 
                    break
            else: 
                break  
        if seen == wordBag:  
            res.append(i)
    return res