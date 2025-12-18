"""
QUESTION:
Write a function `find_frequency` that takes a tuple `t` and a variable `k` as input and returns the frequency of `k` in `t` or any nested tuples within `t`. The function should recursively traverse the tuple and its nested tuples, counting the occurrences of `k`. Note that the function should perform an exact match, i.e., it will not match integer 2 with float 2.0.
"""

def find_frequency(t, k):
    count = 0

    for i in t:
        if type(i) == tuple:
            count += find_frequency(i, k)
        else:
            if i == k:
                count += 1

    return count