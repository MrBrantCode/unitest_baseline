"""
QUESTION:
Given a list of strings `words` from an alien language's dictionary, a list of frequencies `freq` for each word in `words`, and a list of constraints `constraints` where each constraint is a pair of characters, return a string of the unique letters in the new alien language sorted in lexicographically increasing order by the new language's rules. If there is no solution, return `""`. If there are multiple solutions, return any of them.

The function should be named `alienOrder` and take three parameters: `words`, `freq`, and `constraints`. The function should return a string. 

The input `words` is a list of strings, each consisting of only lowercase English letters. The input `freq` is a list of integers, each corresponding to the frequency of the word at the same index in `words`. The input `constraints` is a list of pairs of unique lowercase English letters, where the first character is lexicographically smaller than the second character in the alien language.

The function should respect the following constraints:
- `1 <= words.length, freq.length <= 100`
- `1 <= words[i].length <= 100`
- `0 <= constraints.length <= 100`
"""

from collections import defaultdict, deque, Counter

def alienOrder(words, freq, constraints):
    # create nodes
    chars = set(''.join(words))
    nodes = {c: {'in': set(), 'out': set()} for c in chars}

    # compare each pair of words and add edges
    for word1, word2 in zip(words, words[1:]):
        for ch1, ch2 in zip(word1, word2):
            if ch1 != ch2:
                nodes[ch2]['in'].add(ch1)
                nodes[ch1]['out'].add(ch2)
                break
        else:
            if len(word2) < len(word1):
                return ""

    # add edges for constraints
    for ch1, ch2 in constraints:
        nodes[ch2]['in'].add(ch1)
        nodes[ch1]['out'].add(ch2)

    # count indegree
    indegree = Counter({node: len(edges['in']) for node, edges in nodes.items()})

    # put all nodes with 0 indegree into queue
    q = deque(node for node, count in indegree.items() if count == 0)

    # topological sort
    res = []
    while q:
        curr = q.popleft()
        res.append(curr)

        for neighbor in nodes[curr]['out']:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                q.append(neighbor)

    # if all nodes are sorted, return the result
    if len(res) == len(nodes):
        return ''.join(res)
        
    # if there is a cycle, return ""
    return ""