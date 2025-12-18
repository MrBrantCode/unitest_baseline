"""
QUESTION:
Implement the `alienOrder` function, which takes a list of words and a list of constraints as input and returns a string representing the correct order of characters in an alien language. 

In this language, the order of characters is determined by the order in which they appear in the given list of words, as well as a list of additional constraints in the form of pairs of characters. If it is impossible to determine a valid order, return an empty string. 

The function should use topological sorting to find a valid order. If there is a cycle in the graph, a valid order does not exist and an empty string should be returned.
"""

from collections import defaultdict, deque, Counter

def alienOrder(words, constraints):
    # Create nodes
    chars = set(''.join(words))
    nodes = {c: {'in': set(), 'out': set()} for c in chars}

    # Compare each pair of words and add edges
    for word1, word2 in zip(words, words[1:]):
        for ch1, ch2 in zip(word1, word2):
            if ch1 != ch2:
                nodes[ch2]['in'].add(ch1)
                nodes[ch1]['out'].add(ch2)
                break
            else:
                if len(word2) < len(word1):
                    return ""

    # Add edges for constraints
    for ch1, ch2 in constraints:
        nodes[ch2]['in'].add(ch1)
        nodes[ch1]['out'].add(ch2)

    # Count indegree
    indegree = Counter({node: len(edges['in']) for node, edges in nodes.items()})

    # Put all nodes with 0 indegree into queue
    q = deque(node for node, count in indegree.items() if count == 0)

    # Topological sort
    res = []
    while q:
        curr = q.popleft()
        res.append(curr)

        for neighbor in nodes[curr]['out']:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                q.append(neighbor)

    # If all nodes are sorted, return the result
    if len(res) == len(nodes):
        return ''.join(res)

    # If there is a cycle, return ""
    return ""