"""
QUESTION:
Write a function `median` that takes a list `l` and a comparison function `cmp_func` as input and returns the median of the list. The function should be able to handle both even and odd length lists. The comparison function `cmp_func` takes two elements as input and returns a value less than, equal to, or greater than zero if the first element is less than, equal to, or greater than the second element.
"""

def median(l: list, cmp_func: callable):
    length = len(l)

    def pivot_fn(left, right):
        mid = (right + left) // 2
        s = sorted([(l[left], left), (l[mid], mid), (l[right], right)], key=lambda x: x[0])
        return s[1][1]

    def partition(left, right, pivot):
        l[pivot], l[right] = l[right], l[pivot]
        j = left

        for i in range(left, right):
            if cmp_func(l[i], l[right]) < 0:
                l[i], l[j] = l[j], l[i]
                j += 1

        l[right], l[j] = l[j], l[right]
        return j

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

    if length % 2 != 0:
        return select(0, length - 1, length // 2)
    else:
        return 0.5 * (select(0, length - 1, length // 2 - 1) + select(0, length - 1, length // 2))