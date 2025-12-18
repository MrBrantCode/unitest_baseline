"""
QUESTION:
Write a function `manipulate_list` that takes two lists of integers `lst1` and `lst2` as input, and returns a new list. The function should first separate the even numbers from `lst1`, sort the remaining odd numbers in descending order, and then combine and sort the numbers in ascending order. Then, it should filter out the even numbers from `lst2`, sort the remaining odd numbers in ascending order, and finally combine the results of both operations into a single list. The function should use constant variables within each sub-function.
"""

def manipulate_list(lst1, lst2):
    temp1 = []
    temp2 = []
    for i in lst1:
        if i % 2 == 0:
            temp1.append(i)
        else:
            temp2.append(i)
    temp2 = sorted(temp2, reverse=True)
    temp1.extend(temp2)
    res1 = list(set(temp1))
    res1.sort()
    temp2 = []
    for i in lst2:
        if i % 2 != 0:
            temp2.append(i)
    res2 = list(set(temp2))
    res2.sort()
    return res1 + res2