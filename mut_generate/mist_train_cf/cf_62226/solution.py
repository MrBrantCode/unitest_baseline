"""
QUESTION:
Create a function `combinationFunc(seq)` that generates all distinct quadruple combinations from the input sequence `seq`. The function should return a list of unique quadruples where order does not matter.
"""

import itertools

def combinationFunc(seq):
    result = list(itertools.combinations(seq, 4))
    result = [tuple(sorted(x)) for x in result] 
    return list(set(result))