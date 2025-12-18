"""
QUESTION:
Create a function `smallest_variation_in_subgroup(arr, limit, subset)` that calculates the smallest quantity of transformations required to convert the array into a palindromic array allowing no more than 'limit' distinct element alterations, employing only constituents from the subgroup. A palindromic array is perceived identically in both directions. One may modify one array constituent to any other constituent from the subgroup per alteration. 

The function should return the total number of changes made if it manages to make the array palindromic successfully. If it runs into a situation where it has to make more changes than the limit allows, it should return -1.
"""

def smallest_variation_in_subgroup(arr, limit, subset):
    counts = dict()
    for a in arr:
        counts[a] = counts.get(a, 0) + 1

    to_subtract = [k for k, v in counts.items() if k in subset and v < len(arr) // 2]
    to_subtract.sort(key=counts.get)

    idx = 0
    while idx < len(to_subtract) and limit > 0:
        limit -= 1
        arr[arr.index(to_subtract[idx])] = to_subtract[-1]
        counts[to_subtract[idx]] -= 1
        counts[to_subtract[-1]] += 1
        if counts[to_subtract[idx]] < len(arr) // 2:
            idx += 1

    if idx < len(to_subtract):
        return -1

    max_subset_elm = max(counts.keys(), key=lambda x: counts[x] if x in subset else -1)
    return sum([v for k, v in counts.items() if k != max_subset_elm])