"""
QUESTION:
Write a function `count_distinct_substrings(S, T)` that takes two strings `S` and `T` as input and returns the number of distinct substrings of `T` that are present in `S`. The function should be case sensitive and should not include any duplicate substrings in the count.
"""

def count_distinct_substrings(S, T):
    # create an empty set to store the distinct substrings
    distinct_substrings = set()
    
    # iterate over the length of string T
    for i in range(len(T)):
        # get each substring of T that exists in S
        for j in range(i, len(T)):
            substring = T[i:j+1]
            if substring in S:
                # add the substring to the set 
                distinct_substrings.add(substring)

    return len(distinct_substrings)