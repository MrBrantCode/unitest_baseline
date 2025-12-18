"""
QUESTION:
Create a function `add_lists(list1, list2)` that takes two lists of integers, `list1` and `list2`, as input and returns a new list containing their element-wise addition. The function should handle lists of varying lengths. The lists contain at most 10^3 integers, and each integer is between 0 and 10^9.
"""

def add_lists(list1, list2):
    output = []
    len1, len2 = len(list1), len(list2)
    max_len = max(len1, len2)

    for i in range(max_len):
        try:
            output.append(list1[i] + list2[i])
        except IndexError:
            if len1 > len2:
                output.append(list1[i])
            else:
                output.append(list2[i])

    return output