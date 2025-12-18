"""
QUESTION:
Create a function `func(arr, num, flag)` that accepts three parameters: an array of unique integers `arr`, an integer to search `num`, and a boolean parameter `flag`. 

If `flag` is False, return the index of the smallest integer in `arr` that is larger than or equal to `num`. If `flag` is True, return the index of the largest integer in `arr` that is smaller than or equal to `num`. 

In both cases, if no suitable integer exists, return -1. The function should handle erroneous input gracefully and log meaningful error messages.
"""

def entrance(arr, num, flag):
    if isinstance(arr, list) and all(isinstance(i, int) for i in arr) and isinstance(num, int) and isinstance(flag, bool):
        if flag:
            arr = sorted([i for i in arr if i <= num])
            if arr:
                return arr.index(max(arr))
            else:
                return -1
        else:
            arr = sorted([i for i in arr if i >= num])
            if arr:
                return arr.index(min(arr))
            else:
                return -1
    else:
        return "Error: Invalid input(s)"