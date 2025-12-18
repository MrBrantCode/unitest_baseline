"""
QUESTION:
Write a function `find_top_k_highest_numbers` that takes an array of integers `arr` and an integer `k` as input, and returns the top `k` highest numbers in the array. The function should not use any built-in sorting algorithms or functions, and should have a time complexity of O(n log k), where `n` is the size of the array.
"""

def find_top_k_highest_numbers(arr, k):
    top_k = []
    for num in arr:
        if len(top_k) < k:
            top_k.append(num)
        else:
            min_num = min(top_k)
            if num > min_num:
                top_k.remove(min_num)
                top_k.append(num)
    return top_k