"""
QUESTION:
Implement a function `strangeSorting(lst)` that sorts a list of real numbers or strings representing numbers in a specific way. The function should follow these rules:

- Start with the smallest value.
- Find the largest value still in the list.
- Find the next smallest value not yet chosen from the list.
- Continue this pattern until all numbers have been selected.
- If the list contains duplications of the smallest or the largest number, the function should place all instances of that number at the start (for smallest) or at the end (for largest) of the sequence respectively.
- The function should work with both lists of real numbers and lists of strings representing numbers. If a string cannot be converted to a number, it should be ignored.

The function should handle lists of various lengths, including empty lists.
"""

def strange_sorting(lst):
    res = []
    lst_float = []
    for item in lst:
        try:
            lst_float.append(float(item))
        except ValueError:
            pass
    if lst_float == []:
        return res
    lst_float.sort()
    while len(lst_float) > 0:
        min_num = min(lst_float)
        while min_num in lst_float:
            res.append(min_num)
            lst_float.remove(min_num)
        if len(lst_float) > 0:
            max_num = max(lst_float)
            while max_num in lst_float:
                lst_float.remove(max_num)
            res.append(max_num)  
    return res