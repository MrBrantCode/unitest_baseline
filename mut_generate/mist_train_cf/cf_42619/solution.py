"""
QUESTION:
Implement a function `applyCut` that takes a hypothesis validity check function `isHypoValid` and a `genMatchSumDR` value as input and returns a boolean indicating whether an event passes the cut criteria based on the hypothesis validity and `genMatchSumDR` being less than 999. The `isHypoValid` function should be implemented to check if the given hypothesis is 'kGenMatch'.
"""

def applyCut(isHypoValid, genMatchSumDR):
    return isHypoValid('kGenMatch') and genMatchSumDR < 999