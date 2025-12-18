"""
QUESTION:
Write a function `countCharacters` that takes a list of strings `words` and a string `chars` as input. A string is considered good if it can be formed by characters from `chars` in the same order as they appear in `chars`. Return the sum of lengths of all good strings in `words`. The function should handle up to 1000 words and 100 characters in each word and `chars`. All strings contain lowercase English letters only.
"""

def countCharacters(words, chars):
    charsList = list(chars)
    result = 0
    for word in words:
        copyList = charsList.copy()
        for i in range(len(word)):
            if word[i] in copyList:
                copyList.remove(word[i])
            else:
                break
        else:
            result += len(word)
    return result