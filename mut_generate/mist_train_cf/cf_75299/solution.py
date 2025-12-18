"""
QUESTION:
Write a function `subarray_count` that takes a string as input and returns the cumulative count of all possible continuous sub-arrays that can be formed from the string. The function should be case-insensitive and consider the input string as a sequence of characters. The characters in each sub-array should be in alphabetical order.
"""

def subarray_count(string):
    string = "".join(sorted(list(string.lower())))
    count = {}
    length = len(string)

    for i in range(length):
        sub = ""
        for j in range(i, length):
            sub = "".join(sorted(list(sub + string[j])))
            count[sub] = count.get(sub, 0) + 1
    cumulative_count = 0
    for i in count:
        cumulative_count += count[i]
    return cumulative_count