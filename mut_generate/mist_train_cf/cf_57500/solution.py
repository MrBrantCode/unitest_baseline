"""
QUESTION:
Write a function `calculate_synonyms` that takes two parameters, `lexicon` and `synonym_pairs`, where `lexicon` is a dictionary mapping words to their direct synonyms and `synonym_pairs` is a list of tuples representing indirect synonym relationships. The function should return a dictionary where each key is a word and its corresponding value is the total number of direct and indirect synonyms it has. The function should avoid circular references and have a time complexity not exceeding O(n log(n)).
"""

from collections import defaultdict

def calculate_synonyms(lexicon, synonym_pairs):
    # Create a graph from lexicon and synonym pairs
    graph = defaultdict(set)
    for word, synonyms in lexicon.items():
        for synonym in synonyms:
            graph[word].add(synonym)
            graph[synonym].add(word)
    for word1, word2 in synonym_pairs:
        graph[word1].add(word2)
        graph[word2].add(word1)
    
    # Perform DFS on each word of the graph to count synonyms
    result = {}
    for word in graph:
        visited = set()
        synonyms = set()
        stack = [word]
        while stack:
            current_word = stack.pop()
            if current_word not in visited:
                visited.add(current_word)
                synonyms.add(current_word)
                stack.extend(synonym for synonym in graph[current_word] if synonym not in visited)
        # Remove the word itself from the synonym count
        synonyms.remove(word)
        result[word] = len(synonyms)
    
    return result