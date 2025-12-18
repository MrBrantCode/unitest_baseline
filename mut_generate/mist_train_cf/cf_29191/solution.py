"""
QUESTION:
Implement the `length` function, which takes two parameters: `t1`, a list of integers, and `n`, an integer representing the length of `t1`. The function should return the length of the longest consecutive subsequence in `t1`.
"""

def length(t1, n):
    t1_set = set(t1)
    max_length = 0

    for num in t1_set:
        if num - 1 not in t1_set:
            current_num = num
            current_length = 1

            while current_num + 1 in t1_set:
                current_num += 1
                current_length += 1

            max_length = max(max_length, current_length)

    return max_length