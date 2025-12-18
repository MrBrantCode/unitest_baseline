"""
QUESTION:
Implement a function `radix_sort` that takes a list of integers as input and returns the list sorted in ascending order using the radix sort algorithm. The function should handle lists of non-negative integers and sort them digit by digit from least significant to most significant digit.
"""

def radix_sort(lst):
    RADIX = 10
    max_length = False
    tmp, placement = -1, 1

    while not max_length:
        max_length = True
        buckets = [list() for _ in range(RADIX)]
        for i in lst:
            tmp = i // placement
            buckets[tmp % RADIX].append(i)
            if max_length and tmp > 0:
                max_length = False
        a = 0
        for b in range(RADIX):
            buck = buckets[b]
            for i in buck:
                lst[a] = i
                a += 1
        placement *= RADIX
    return lst