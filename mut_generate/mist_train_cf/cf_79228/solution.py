"""
QUESTION:
Implement a function `median` that calculates the median of a list of elements using a custom comparison function `cmp_func`. The function should take in a list `l` and a comparison function `cmp_func` as arguments. The comparison function should take two elements `x` and `y` and return a negative value if `x` is less than `y`, zero if `x` is equal to `y`, and a positive value if `x` is greater than `y`. The function should return the median of the list, handling both the cases where the list length is odd and even.
"""

def median(l: list, cmp_func: callable):
    def get_Nth(l, N, cmp_func):
        if len(l) <= 1:  
            return l[0]
        pivot = l[len(l) // 2]  
        less = [x for x in l if cmp_func(x, pivot) < 0]
        equal = [x for x in l if cmp_func(x, pivot) == 0]
        greater = [x for x in l if cmp_func(x, pivot) > 0]
        if N < len(less):  
            return get_Nth(less, N, cmp_func)
        elif N < len(less) + len(equal):  
            return pivot
        else:  
            return get_Nth(greater, N - len(less) - len(equal), cmp_func)

    l = l.copy()  
    if len(l) % 2:
        return get_Nth(l, len(l) // 2, cmp_func)  
    else:
        return (get_Nth(l, len(l) // 2 - 1, cmp_func) + get_Nth(l, len(l) // 2, cmp_func)) / 2  