"""
QUESTION:
Implement a function called `median` that takes a list `l` and a comparison function `cmp_func` as parameters. The function should return the median of the elements in the list without using built-in sorting functions or methods. The function should be able to handle lists with both even and odd numbers of elements, manage duplicates, and use the provided comparison function for performing comparisons. The function should not use any sorting techniques or built-in functionalities.
"""

def median(l: list, cmp_func: callable):
    length = len(l)
    
    # Choose pivot
    def pivot_fn(left, right):
        mid = (right - left) // 2 + left
        s = sorted([(l[left], left), (l[mid], mid), (l[right], right)], key=lambda x: x[0])
        return s[1][1]

    # Partition
    def partition(left, right, pivot):
        l[pivot], l[right] = l[right], l[pivot]
        j = left

        for i in range(left, right):
            if cmp_func(l[i], l[right]) < 0:
                l[i], l[j] = l[j], l[i]
                j += 1

        l[right], l[j] = l[j], l[right]
        return j

    # Select
    def select(left, right, k):
        if left == right:
            return l[left]
        pivot = pivot_fn(left, right)
        pivot = partition(left, right, pivot)

        if k == pivot:
            return l[k]
        elif k < pivot:
            return select(left, pivot - 1, k)
        else:
            return select(pivot + 1, right, k)

    # Finding median
    if length % 2 != 0:
        return select(0, length - 1, length //2 )
    else:
        return 0.5 * (select(0, length - 1, length // 2 - 1) + select(0, length - 1, length // 2))