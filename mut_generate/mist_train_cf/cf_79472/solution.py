"""
QUESTION:
Create a function `correct_solution(lst, mode)` that takes a non-empty list of integers `lst` and a boolean parameter `mode` as input. The function should return the sum of either even integers at odd indexed places or odd integers at even indexed places in the list, depending on the value of `mode`. If `mode` is `True`, the function should return the sum of even integers at odd indexed places. If `mode` is `False`, the function should return the sum of odd integers at even indexed places.
"""

def correct_solution(lst, mode): 
    result = 0
    for i in range(len(lst)):
        if mode: # Even integers sum at odd indices
            if i % 2 != 0 and lst[i] % 2 == 0:
                result += lst[i]
        else: # Odd integers sum at even indices
            if i % 2 == 0 and lst[i] % 2 != 0:
                result += lst[i]
    return result