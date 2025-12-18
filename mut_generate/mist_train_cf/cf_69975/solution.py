"""
QUESTION:
Create a function `median` that takes a list `l` and a comparison function `cmp_func` as parameters. The function should return the median of the list without using list sorting or built-in sorting functions. It should handle lists with both even and odd numbers of elements, as well as lists with duplicate values and empty lists. The function should use the provided comparison function `cmp_func` for comparisons. The function should return `None` for an empty list.
"""

def median(l: list, cmp_func: callable):
    if not l:
        return None
    dict_val = {i: l.count(i) for i in l}
    dict_val = dict(sorted(dict_val.items(), key=lambda item: cmp_func(0, item[0])))
    cum_sum = 0
    for k, v in dict_val.items():
        cum_sum += v
        if cum_sum >= len(l) / 2:
            break
    if len(l) % 2 == 0:
        if cum_sum - v < len(l) / 2:
            return k
        else:
            for key in dict_val.keys():
                if cmp_func(key, k) == 0:
                    return (key + k) / 2
    else:
        return k