"""
QUESTION:
Given a unique binary sequence `S` of maximum length 50, where the count of 0's is identical to the count of 1's and every initial segment contains at least an equal number of 1's as 0's, write a function `optimize_binary(S)` to find the lexicographically superior sequence that can be achieved after any number of moves, where a move is defined as interchanging two adjacent, non-empty, unique sub-sequences of `S`.
"""

def optimize_binary(s: str) -> str:
    stack = []
    for c in s:
        if c == '1':
            stack.append(c)
        else: # c == '0'
            zeros = [c]
            while stack and stack[-1] == '0': # pop zeros from stack
                stack.pop()
                zeros.append('0')
            stack.append(''.join(zeros)) # after popping zeros, append one '0'
    return ''.join(stack)