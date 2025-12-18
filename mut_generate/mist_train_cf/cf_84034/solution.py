"""
QUESTION:
Write a function called `distinct_subsequences` that takes a string sequence `seq` of up to 1000 characters as input and returns the cumulative count of distinct non-redundant subsequences. The function should be optimized to handle large strings efficiently and minimize memory usage.
"""

def distinct_subsequences(seq):
    distinct_subsequences_set = set()
    
    n = len(seq)
    for length in range(1, n + 1):
        for i in range(n - length + 1):
            j = i + length
            substr = seq[i:j]
            if substr not in distinct_subsequences_set:
                distinct_subsequences_set.add(substr)
    
    return len(distinct_subsequences_set)