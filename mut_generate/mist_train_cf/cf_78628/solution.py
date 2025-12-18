"""
QUESTION:
Write a function `shortestDistance(wordsDict, word1, word2)` that takes a list of strings `wordsDict` and two distinct strings `word1` and `word2` as input, and returns the smallest distance between these two words in the list. The length of `wordsDict` is between 1 and 3 * 10^4, the length of each string in `wordsDict` is between 1 and 10, and both `word1` and `word2` are elements of `wordsDict`. `word1` and `word2` are not equal.
"""

def shortestDistance(wordsDict, word1, word2):
    index1, index2 = -1, -1
    minDistance = len(wordsDict)
    
    for i, word in enumerate(wordsDict):
      if word == word1:
          index1 = i
      elif word == word2:
          index2 = i

      if index1 != -1 and index2 != -1:
          minDistance = min(minDistance, abs(index1 - index2))
          
    return minDistance