"""
QUESTION:
Find the longest progressively ascending subsequence in an array of integers and its starting index. The array may contain duplicate numbers. The function should return the subsequence and its starting index. In case of multiple subsequences with the same maximum length, return the one that appears first. The function should be able to handle arrays with zero or one element.
"""

def entrance(seq):
    if not seq:
        return []

    seq = list(seq)
    len_seq = len(seq)

    length = [1] * len_seq
    prev = [None] * len_seq

    for i in range(1, len_seq):
        for j in range(i):
            if seq[i] > seq[j] and length[i] <= length[j]:
                length[i] = length[j] + 1
                prev[i] = j

    max_length_idx = max(range(len_seq), key=length.__getitem__)
    subseq_indexes = []
    while max_length_idx is not None:
        subseq_indexes.append(max_length_idx)
        max_length_idx = prev[max_length_idx]

    subseq_indexes.reverse()

    return [seq[i] for i in subseq_indexes], subseq_indexes[0]