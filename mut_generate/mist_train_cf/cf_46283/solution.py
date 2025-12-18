"""
QUESTION:
Write a function `pack_duplicates(lst)` to pack consecutive duplicates of elements in the given list into sublists, including handling nested lists. The function should work recursively on nested lists and assume they are also sorted.
"""

def pack_duplicates(lst):
    result = []
    for i in range(len(lst)):
        if type(lst[i]) is list:
            result.append(pack_duplicates(lst[i]))
        else:
            if i == 0 or lst[i] != lst[i-1]:
                result.append([lst[i]])
            else:
                result[-1].append(lst[i])
    return result