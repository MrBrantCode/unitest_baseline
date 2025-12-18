"""
QUESTION:
Create a function `customized_median(l, cmp_func)` that calculates the median of the elements in list `l` without using any sorting techniques or built-in functionalities. The function should be able to handle tuples with both odd and even count of elements, manage duplicates efficiently, and incorporate a comparison function `cmp_func` for effective comparisons. The function should return the median value. The list `l` can contain duplicate elements and the comparison function `cmp_func` should take two arguments and return a negative value if the first argument is less than the second, zero if the arguments are equal, and a positive value if the first argument is greater than the second.
"""

def customized_median(l, cmp_func):
    n = len(l)
    def partition(low, high):
        pivot = l[high]
        i = (low - 1)

        for j in range(low, high):
            if cmp_func(l[j], pivot) < 0:
                i = i + 1
                l[i], l[j] = l[j], l[i]
        l[i + 1], l[high] = l[high], l[i + 1]
        return (i + 1)

    def quick_select(low, high, k):
        if (k > 0 and k <= high - low + 1):
            index = partition(low, high)

            if (index - low == k - 1):
                return l[index]
            if (index - low > k - 1):
                return quick_select(low, index - 1, k)

            return quick_select(index + 1, high, k - index + low - 1)

        return float('inf')
    
    if n % 2 == 0:
        return (quick_select(0, n - 1, n // 2) +
                quick_select(0, n - 1, n // 2 + 1)) / 2.0
    else:
        return quick_select(0, n - 1, n // 2 + 1)