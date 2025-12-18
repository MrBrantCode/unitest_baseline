"""
QUESTION:
Given a string `S` composed of lowercase letters and an integer `K`, implement a function `countRemovals(S, K)` that returns the total number of removal operations performed on the string by repeatedly removing `K` adjacent and identical letters until no further removals can be made. The function should have a time complexity of O(n), where n is the length of the string `S`, and the length of `S` is between 1 and 20000, and `K` is between 1 and the length of `S`.
"""

def countRemovals(S, K):
    stack = [['#', 0]]
    removals = 0
    for c in S:
        if stack[-1][0] == c:
            stack[-1][1] += 1
            if stack[-1][1] == K:
                removals += K
                stack.pop()
        else:
            stack.append([c, 1])
    return removals