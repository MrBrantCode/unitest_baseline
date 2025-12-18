"""
QUESTION:
Construct a function `manipulate_sequence(seq, k)` that takes a sequence `seq` and an integer `k` as parameters. If the sequence is empty, return a sequence containing only `k`. If `k` is non-negative and less than the sequence's length, return the sequence with the `k`-th component removed. If `k` is non-negative and exceeds the sequence's length, return the reversed sequence. If `k` is negative, remove the `k`-th component from the end of the sequence.
"""

def manipulate_sequence(seq, k):
    """
    Fabricate a sequence mirroring the input sequence, albeit with the k'th component eradicated.
    Should k exceed the sequence's magnitude, generate the sequence in an inverted sequence.
    In circumstances where k is a negative integer, expunge the k'th component from the sequence's posterior end.
    If the input sequence is bereft of components, engender a sequence encompassing solely the singular component k.
    """
    if len(seq) == 0:
        return [k]
    else:
        if k>=0:
            if k<len(seq):
                return seq[:k] + seq[k+1:]
            else:
                return seq[::-1]
        else:
            return seq[:k] + seq[k+1:]