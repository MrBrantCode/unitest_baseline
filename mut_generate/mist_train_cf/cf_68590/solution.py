"""
QUESTION:
Write a function called `unique_items` that removes all duplicate elements from a given list of integers and returns the modified list in descending order. The function should not use any built-in `unique()` or `set()` method. 

The input list will have a length of at least 1 and at most 10^4, and each integer in the input list will be in the range [-10^6, 10^6]. The function signature is `def unique_items(arr: List[int]) -> List[int]`.
"""

def unique_items(arr: list[int]) -> list[int]:
    arr_dict = dict.fromkeys(arr, 0)
    unique_list = sorted(list(arr_dict.keys()), reverse=True)
    return unique_list