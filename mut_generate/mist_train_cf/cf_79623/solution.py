"""
QUESTION:
Create a function `areSentencesSimilarTwo` that determines if two phrases are alike based on a compilation of analogous word pairs. The function takes three parameters: two phrases `words1` and `words2` as lists of strings, and a list of analogous word pairs `pairs`. Return `True` if the phrases are alike, `False` otherwise. The phrases can only be alike if they contain the same quantity of words. The similarity relation is transitive and symmetric, and a word is always alike with itself. The length of `words1` and `words2` will not surpass 1000, the length of `pairs` will not surpass 2000, and the length of each word will be within the range [1, 20].
"""

def areSentencesSimilarTwo(words1, words2, pairs):
    if len(words1) != len(words2): return False

    graph = {}
    for w1, w2 in pairs:
        if w1 not in graph: graph[w1] = w1
        if w2 not in graph: graph[w2] = w2
        union(graph, w1, w2)

    for w1, w2 in zip(words1, words2):
        if w1 not in graph or w2 not in graph or find(graph, w1) != find(graph, w2):
            return False

    return True

def find(graph, word):
    if graph[word] != word:
        graph[word] = find(graph, graph[word])
    return graph[word]

def union(graph, word1, word2):
    root1 = find(graph, word1)
    root2 = find(graph, word2)
    graph[root2] = root1