"""
QUESTION:
Create a function `alienOrder` that takes two parameters, `words` and `constraints`. `words` is a list of strings representing an alien's vocabulary and `constraints` is a list of lists where each sublist contains a pair of characters, the first character should come before the second character in the alien's alphabet. The function should return the lexicographically smallest possible order of the alien's alphabet. If there is no valid order, return an empty string.
"""

from collections import defaultdict, deque

def alienOrder(words, constraints):
    # Step 0: create data structures, the indegree of each unique letter to 0.
    adj_list = defaultdict(set)
    in_degree = {c : 0 for word in words for c in word}

    # Step 1: We need to populate adj list and in_degree.
    for i in range(len(words) - 1):
        word1 = words[i]
        word2 = words[i+1]
        for c, d in zip(word1, word2):
            if c != d:
                if d not in adj_list[c]:
                    adj_list[c].add(d)
                    in_degree[d] += 1
                break
            else:
                if len(word1) > len(word2):
                    return ''

    # Include all constraints
    for constraint in constraints:
        if constraint[1] not in adj_list[constraint[0]]:
            adj_list[constraint[0]].add(constraint[1])
            in_degree[constraint[1]] += 1

    # Step 2: We need to repeatedly pick off nodes that have no incoming edges and remove edges.
    output = []
    queue = deque([c for c in in_degree if in_degree[c] == 0])
    while queue:
        c = queue.popleft()
        output.append(c)
        for d in adj_list[c]:
            in_degree[d] -= 1
            if in_degree[d] == 0:
                queue.append(d)

    # If not all letters are in output, that means there was a cycle and so
    # no valid ordering. Return "" as per the problem description.
    if len(output) < len(in_degree):
        return ""
    else:
        return ''.join(output)