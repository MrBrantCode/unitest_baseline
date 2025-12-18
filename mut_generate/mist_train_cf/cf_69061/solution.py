"""
QUESTION:
Create a function `enhance_seq(arr)` that takes a list of distinct integers as input and returns a list of tuples. Each tuple contains the highest index of an element that is not less than the subsequent element and the index of the closest superior element that can be swapped to improve the sequence. If no such element is found, return [(pos: -1, exchange_with: -1)].
"""

def enhance_seq(arr):
    exchange_list = []
    
    for i in range(len(arr) - 1):
        if arr[i] >= arr[i + 1]:
            exchange_with = -1
            for j in range(i + 2, len(arr)):
                if arr[j] > arr[i + 1]:
                    exchange_with = j
                    break
            exchange_list.append((i + 1, exchange_with if exchange_with != -1 else -1))

    return exchange_list if exchange_list else [(pos := -1, exchange_with := -1)]