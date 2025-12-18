"""
QUESTION:
Write a function `removeDuplicates(S, K)` that takes a string `S` and an integer `K` as input. The function should return the final string after all possible duplicate removals have been executed, where a duplicate removal involves selecting `K` adjacent and identical letters, and eradicating them. The process of duplicate removal on `S` is repeated until no further removals can be made. The input string `S` is composed solely of English lowercase letters, and its length is between 1 and 20000 (inclusive). The value of `K` is between 1 and the length of `S` (inclusive).
"""

def removeDuplicates(S: str, K: int) -> str:
    stack = []
    for char in S:
        if stack and stack[-1][0] == char:
            stack[-1][1] += 1
            if stack[-1][1] == K:
                stack.pop()
        else:
            stack.append([char, 1])
    return ''.join(char * count for char, count in stack)