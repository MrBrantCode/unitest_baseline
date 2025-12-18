"""
QUESTION:
Write a function named `areSentencesSimilar(sentence1, sentence2, similarPairs)` that determines whether two sentences are similar. The sentences are represented as arrays of words, and two words are considered similar if they are in the `similarPairs` list. Two sentences are similar if they have the same length and each word in `sentence1` is similar to the corresponding word in `sentence2`. The function should return `True` if the sentences are similar and `False` otherwise. The function has the following constraints: `1 <= sentence1.length, sentence2.length <= 1000`, `1 <= sentence1[i].length, sentence2[i].length <= 20`, and `0 <= similarPairs.length <= 1000`.
"""

def areSentencesSimilar(sentence1, sentence2, similarPairs):
    if len(sentence1) != len(sentence2):
        return False

    similar_dict = {}
    for pair in similarPairs:
        if pair[0] not in similar_dict:
            similar_dict[pair[0]] = set()
        if pair[1] not in similar_dict:
            similar_dict[pair[1]] = set()
        similar_dict[pair[0]].add(pair[1])
        similar_dict[pair[1]].add(pair[0])

    for word1, word2 in zip(sentence1, sentence2):
        if word1 == word2:
            continue
        if word1 not in similar_dict or word2 not in similar_dict[word1]:
            return False
    return True