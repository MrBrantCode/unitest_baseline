"""
QUESTION:
Create a function named `common` that takes two lists of integers `l1` and `l2` as input and returns a list of unique common elements in sorted order. The function should not use Python's built-in list functionalities for finding common elements or removing duplicates. It should be able to handle lists containing negative numbers. The input lists are not guaranteed to be sorted.
"""

def common(l1: list, l2: list) -> list:
    result = []
    seen = set()
    l1.sort()
    l2.sort()

    def binary_search(l: list, x: int) -> bool:
        low = 0
        high = len(l) - 1

        while low <= high:
            mid = (low + high) // 2

            if l[mid] < x:
                low = mid + 1
            elif l[mid] > x:
                high = mid - 1
            else:
                return True

        return False

    for num in l1:
        if num not in seen and binary_search(l2, num):
            result.append(num)
            seen.add(num)

    return result