"""
QUESTION:
Create a function `rotate_list(lst, k)` that takes a list of elements (which can be strings or numbers) and an integer `k` as input, and returns the list rotated to the right by `k` positions. If `k` exceeds the length of the list, implement the rotation as if `k` was the remainder of `k` divided by the length of the list. Handle errors for cases where the list is `None`, the list is empty, `k` is `None`, or `k` is negative.
"""

def rotate_list(lst, k):
    if lst is None or k is None:
        return "Error: Both the list and rotation count must be provided."
  
    n = len(lst)
  
    if n == 0:
        return "Error: The list cannot be empty."
  
    k = k % n if k >= 0 else n + k % n
  
    return lst[-k:] + lst[:-k]