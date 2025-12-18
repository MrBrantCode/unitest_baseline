"""
QUESTION:
Write a function `alienOrder` that takes two parameters, `words` and `constraints`, where `words` is a list of strings from an alien dictionary sorted lexicographically by the rules of the new language and `constraints` is a list of pairs of characters where the first character is lexicographically smaller than the second character in the alien language. The function should return a string of the unique letters in the new alien language sorted in lexicographically increasing order by the new language's rules, or an empty string if there is no solution. The input constraints are as follows: 
- 1 <= words.length <= 100 
- 1 <= words[i].length <= 100 
- words[i] consists of only lowercase English letters.
- 0 <= constraints.length <= 100
- Each constraint is a pair of unique lowercase English letters.
"""

from collections import defaultdict, deque

def alienOrder(words, constraints):
    # Create data structures and set the in_degree of each unique letter to 0.
    adj_list = defaultdict(set)
    in_degree = {c : 0 for word in words for c in word}
    
    # Populate adj_list and in_degree.
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
    
    # Include all constraints.
    for constraint in constraints:
        if constraint[1] not in adj_list[constraint[0]]:
            adj_list[constraint[0]].add(constraint[1])
            in_degree[constraint[1]] += 1
    
    # Repeatedly pick off nodes that have no incoming edges and remove edges.
    output = []
    queue = deque([c for c in in_degree if in_degree[c] == 0])
    while queue:
        c = queue.popleft()
        output.append(c)
        for d in adj_list[c]:
            in_degree[d] -= 1
            if in_degree[d] == 0:
                queue.append(d)
                
    # If not all letters are in output, that means there was a cycle and so no valid ordering. Return "".
    if len(output) < len(in_degree):
        return ""
    else:
        return ''.join(output)