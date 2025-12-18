"""
QUESTION:
Write a function `areSentencesSimilar(sentence1, sentence2, similarPairs)` that determines if two sentences `sentence1` and `sentence2` are similar. A sentence is represented as a string array, and two sentences are similar if they have the same length and corresponding words are similar. Two words are similar if they are the same or if they appear in the `similarPairs` array. The `similarPairs` array contains pairs of similar words. 

Constraints: `1 <= sentence1.length, sentence2.length <= 1000`, `1 <= sentence1[i].length, sentence2[i].length <= 20`, and `0 <= similarPairs.length <= 1000`.
"""

def areSentencesSimilar(sentence1, sentence2, similarPairs):
    if len(sentence1) != len(sentence2):
        return False

    pairs = set()
    for pair in similarPairs:
        pairs.add((pair[0], pair[1]))
        pairs.add((pair[1], pair[0]))

    for word1, word2 in zip(sentence1, sentence2):
        if word1 != word2 and (word1, word2) not in pairs:
            return False

    return True