"""
QUESTION:
Write a function `shortestDistance(wordsDict, word1, word2)` that calculates the shortest distance in terms of characters (including spaces) between two given words `word1` and `word2` in a list of strings `wordsDict`. The function should return the minimum distance between these two words. `word1` and `word2` may be the same and are guaranteed to exist in `wordsDict`. The length of `wordsDict` is between 1 and 3 * 10^4, and the length of each word is between 1 and 10.
"""

def shortestDistance(wordsDict, word1, word2):
    i1, i2 = -1, -1
    min_distance = float('inf')
    same_word = word1 == word2

    def calc_dist(i, j):
        if j < i:
            return len(' '.join(wordsDict[j+1:i]))
        else:
            return len(' '.join(wordsDict[i+1:j]))

    for i, word in enumerate(wordsDict):
        if word == word1:
            if same_word and i1 != -1:
                distance = calc_dist(i, i1)
                min_distance = min(min_distance, distance)
            i1 = i
        elif word == word2:
            if i1 != -1:
                distance = calc_dist(i, i1)
                min_distance = min(min_distance, distance)
            i2 = i
    return min_distance