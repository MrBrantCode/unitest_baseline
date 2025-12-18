"""
QUESTION:
Write a function `countRemovals(S, K)` that takes a string `S` consisting of lowercase English alphabets and an integer `K` as input, and returns a tuple containing the final string after all possible removals of `K` consecutive identical characters and the total count of removals. The function should iterate through the string, removing `K` consecutive identical characters until no more removals can be made. The length of the string `S` is between 1 and 20000, and `K` is between 1 and the length of `S`.
"""

def countRemovals(S, K):
    stack = []
    removals = 0
    for c in S:
        if stack and stack[-1][0] == c:
            stack[-1][1] += 1
            if stack[-1][1] == K:
                stack.pop()
                removals += 1
        else:
            stack.append([c, 1])
    return (''.join(c * k for c, k in stack), removals)