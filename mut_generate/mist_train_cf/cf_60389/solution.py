"""
QUESTION:
Write a function `pairs_sum_with_k_difference` that takes two inputs: a list of integers and an integer `k`. It returns `True` if there are two distinct elements in the list whose difference is `k`, and `False` otherwise. The function must have a time complexity of O(n log n).
"""

def pairs_sum_with_k_difference(l: list, k: int):
    l.sort()
    for i in range(len(l)):
        target = l[i] + k
        left, right = 0, len(l) - 1
        while left <= right:
            mid = (left + right) // 2
            if l[mid] == target and mid != i:
                return True
            elif l[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
    return False