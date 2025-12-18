"""
QUESTION:
Write a function `quickselect_median` that calculates the median of a list without using built-in sorting functions or sorting the data. The list may contain tuples, negative integers, and floating point numbers. The function should handle edge case scenarios where multiple medians exist, non-numeric items, and lists with less than two elements. The function should return the median of the input list. The function should not run in constant time, but rather in linear time (O(n)) using the QuickSelect algorithm.
"""

def quickselect_median(nums: list) -> float:
    """Calculates the median of a list without using built-in sorting functions or sorting the data."""
    
    def pivot_fn(l):
        """Selects a pivot element from the list."""
        try:
            assert len(l) != 0
            return l[len(l) // 2]
        except AssertionError:
            print("The provided list contains fewer than two elements!")
            return None
        except TypeError:
            print("The provided list contains one or more non-numeric items!")
            return None

    def quickselect(l: list, k: int) -> float:
        """Finds the k-th smallest element in the list using the QuickSelect algorithm."""
        if len(l) == 1:
            assert k == 0
            return l[0]

        pivot = pivot_fn(l)

        lows = [el for el in l if el < pivot]
        highs = [el for el in l if el > pivot]
        pivots = [el for el in l if el == pivot]

        if k < len(lows):
            return quickselect(lows, k)
        elif k < len(lows) + len(pivots):
            return pivots[0]
        else:
            return quickselect(highs, k - len(lows) - len(pivots))

    if len(nums) % 2 == 1:
        return quickselect(nums, len(nums) // 2)
    else:
        return 0.5 * (quickselect(nums, len(nums) // 2 - 1) +
                      quickselect(nums, len(nums) // 2))