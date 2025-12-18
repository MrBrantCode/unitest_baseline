"""
QUESTION:
Write a function `validate_stack_sequence(pushed, popped, peeked)` that takes three sequences of distinct integers as input, where the sequences are permutations of each other. The function should return `True` if the sequences could have been the result of a sequence of push, pop, and peek operations on an initially empty stack, and `False` otherwise. The peek operation looks at the top item without removing it. The length of each sequence is at most 1000, and the values in the sequences are between 0 and 1000 (exclusive).
"""

def validate_stack_sequence(pushed, popped, peeked):
    stack = []
    pi = 0
    popi = 0
    peeki = 0
    while pi < len(pushed) or stack:
        if not stack or stack[-1] != peeked[peeki]:
            if pi == len(pushed):
                return False
            stack.append(pushed[pi])
            pi += 1
        else:
            peeki += 1
            if stack[-1] == popped[popi]:
                stack.pop()
                popi += 1
    return popi == len(popped)