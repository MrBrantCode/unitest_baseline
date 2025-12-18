"""
QUESTION:
Implement the `dropWhile` function, which takes a sequence and a predicate function as input. The function should return a new sequence with elements dropped based on the predicate until the predicate returns false for the first time. After the predicate returns false, all remaining elements should be included in the resulting sequence. The function should not modify the original sequence.
"""

def dropWhile(sequence, predicate):
    result = []
    drop = True
    for item in sequence:
        if drop and predicate(item):
            continue
        else:
            drop = False
            result.append(item)
    return result