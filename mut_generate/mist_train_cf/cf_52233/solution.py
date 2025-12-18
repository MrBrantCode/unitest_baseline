"""
QUESTION:
Given an array of strings `wordsDict` and two distinct strings `word1` and `word2` that are present in the array, write a function `shortestWordDistance` to determine the smallest distance between these two words in the list. The function should return this minimum distance. The length of `wordsDict` is between 1 and 3 * 10^4, the length of `wordsDict[i]` is between 1 and 10, and `wordsDict[i]` is composed of lowercase English letters.
"""

def shortestWordDistance(wordsDict, word1, word2):
    index1, index2 = -1, -1
    minDistance = len(wordsDict)

    for i in range(len(wordsDict)):
        if wordsDict[i] == word1:
            index1 = i
        elif wordsDict[i] == word2:
            index2 = i

        if index1 != -1 and index2 != -1:
            minDistance = min(minDistance, abs(index1 - index2))

    return minDistance