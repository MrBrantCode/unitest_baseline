"""
QUESTION:
Write a function called `sum_lists` that takes a list of lists as input and returns a single list where each element is the sum of the elements in the corresponding positions of the sublists. If the sublists have different lengths, the function should return `None`.
"""

def sum_lists(lists):
    max_length = max(len(sublist) for sublist in lists)
    result = []
    for i in range(max_length):
        sublist_sum = 0
        for sublist in lists:
            if i < len(sublist):
                sublist_sum += sublist[i]
            else:
                return None
        result.append(sublist_sum)
    return result