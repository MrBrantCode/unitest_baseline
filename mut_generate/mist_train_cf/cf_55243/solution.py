"""
QUESTION:
Write a function called `exchange` that takes two lists `lst1` and `lst2` as input. The function should check if it's possible to make all elements in `lst1` even by swapping elements between `lst1` and `lst2`. The function should return "YES" if possible and "NO" otherwise. The function should assume that the input lists only contain integers.
"""

def exchange(lst1, lst2):
    if sum(lst1) % 2 != 0 or sum(lst2) % 2 != 0:
        return "NO"

    for i in range(len(lst1)):
        if lst1[i] % 2 != 0:
            has_swap = False
            for j in range(len(lst2)):
                if lst2[j] % 2 == 0:
                    lst1[i], lst2[j] = lst2[j], lst1[i]
                    has_swap = True
                    break
            if not has_swap:
                return "NO"

    return "YES"