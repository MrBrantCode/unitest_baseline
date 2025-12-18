"""
QUESTION:
Write a function `median` that calculates the median of a list of elements, which can be either single values or tuples. The function should take two parameters: `l` (the list of elements) and `cmp_func` (a comparison function that takes two elements as input and returns a value that determines their order). The function should handle lists of both even and odd lengths, as well as duplicate elements, without using built-in sorting functions or conventional methodologies for median calculation.
"""

def median(l: list, cmp_func: callable):
    def get_Nth(l, N, cmp_func):
        """Helper function to find the N-th item in the list"""
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