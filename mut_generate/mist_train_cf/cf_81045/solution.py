"""
QUESTION:
Given the origin gene sequence, destination gene sequence, and a gene repository, write a function `minMutation(start, end, bank)` that returns the minimum number of mutations required to mutate from `start` to `end`. The function should return -1 if no such mutation exists. The gene sequences consist of characters 'A', 'C', 'G', 'T'. The origin point is presumed to be valid and may not be included in the repository. All mutations in the sequence must be legitimate.
"""

from collections import deque

def minMutation(start, end, bank):
    if end not in bank:
        return -1
    queue = deque([(start, 0)])
    bank = set(bank)
    while queue:
        (word, steps) = queue.popleft()
        if word == end:
            return steps
        for i in range(len(word)):
            for c in 'ACGT':
                next_word = word[:i] + c + word[i+1:]
                if next_word in bank:
                    bank.remove(next_word)
                    queue.append((next_word, steps + 1))
    return -1