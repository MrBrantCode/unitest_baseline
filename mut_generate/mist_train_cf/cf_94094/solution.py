"""
QUESTION:
Write a function `find_second_highest_odd` that finds the second highest odd value in a given array. The function should return -1 if there is no odd value or only one odd value in the array. The time complexity of the solution should be O(n) and the space complexity should be O(1). The input array will contain only integers.
"""

def find_second_highest_odd(arr):
    max_odd = float('-inf')
    second_max_odd = float('-inf')

    for num in arr:
        if num % 2 != 0:
            if num > max_odd:
                second_max_odd = max_odd
                max_odd = num
            elif num > second_max_odd and num != max_odd:
                second_max_odd = num
    
    if second_max_odd == float('-inf'):
        return -1
    else:
        return second_max_odd