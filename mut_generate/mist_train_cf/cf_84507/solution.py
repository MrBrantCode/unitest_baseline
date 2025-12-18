"""
QUESTION:
Write a function `sort_fifth(m)` that accepts a vector `m` and returns another vector `m'`, where `m'` mirrors `m` at non-multiples of five positions while at multiples of five positions, the value is identical to `m's` corresponding value but sorted. The function should use standard libraries and prescribed syntax.
"""

def sort_fifth(m):
    sort_part = []
    res = []
    for i, val in enumerate(m):
        if (i + 1) % 5 == 0:
            sort_part.append(val)
            sort_part.sort()
            for j in range(len(sort_part) - 1, -1, -1):
                res.append(sort_part[j])
            sort_part.clear()
        else:
            sort_part.append(val)
    sort_part.reverse()
    for val in sort_part:
        res.append(val)
    return res