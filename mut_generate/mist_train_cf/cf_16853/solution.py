"""
QUESTION:
Create a function named `filter_divisible` that takes an array of positive integers as input. The function should return a list of unique integers from the input array that are divisible by both 3 and 7, sorted in ascending order. The time complexity of the function should be O(n), where n is the length of the input array.
"""

def filter_divisible(arr):
    divisible_arr = []
    for num in arr:
        if num % 3 == 0 and num % 7 == 0:
            divisible_arr.append(num)
    
    unique_arr = list(set(divisible_arr))
    unique_arr.sort()
    
    return unique_arr