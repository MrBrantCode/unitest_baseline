"""
QUESTION:
Implement a function `median` that takes a list of numbers as input and returns the median value. The function should handle lists with both even and odd quantities of elements, duplicates, and negative values, and it should not sort the list or use built-in functions like `sort` or `sorted`. Instead, the function should use a custom implementation to find the median. The input list can contain large numbers.
"""

def find_median(lst):
    """
    Custom implementation to find the median of a list of numbers.

    Args:
        lst (list): A list of numbers.

    Returns:
        float: The median value of the input list.
    """
    length = len(lst)
    quick_select = QuickSelect(lst)

    if length % 2 == 0:  # even number of elements
        return (quick_select.find_kth_smallest(length // 2) + 
                quick_select.find_kth_smallest(length // 2 + 1)) / 2
    else:  # odd number of elements
        return quick_select.find_kth_smallest(length // 2 + 1)


class QuickSelect:
    def __init__(self, lst):
        self.lst = lst

    def find_kth_smallest(self, k):
        if len(self.lst) == 1:
            return self.lst[0]

        pivot = self.lst[len(self.lst) // 2]

        left = [x for x in self.lst if x < pivot]
        middle = [x for x in self.lst if x == pivot]
        right = [x for x in self.lst if x > pivot]

        if k <= len(left):
            return QuickSelect(left).find_kth_smallest(k)
        elif k <= len(left) + len(middle):
            return middle[0]
        else:
            return QuickSelect(right).find_kth_smallest(k - len(left) - len(middle))