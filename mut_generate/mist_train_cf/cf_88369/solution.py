"""
QUESTION:
Write a function `find_top_three(arr)` to find the top three highest numbers from an array `arr`. The array `arr` has a maximum of 1000 elements and each element has a maximum value of 1000. The function should not use any sorting algorithm and should have a time complexity of O(n).
"""

def find_top_three(arr):
    highest1 = float('-inf')  # initialize the highest number 1 as negative infinity
    highest2 = float('-inf')  # initialize the highest number 2 as negative infinity
    highest3 = float('-inf')  # initialize the highest number 3 as negative infinity

    for num in arr:
        if num > highest1:
            highest3 = highest2
            highest2 = highest1
            highest1 = num
        elif num > highest2:
            highest3 = highest2
            highest2 = num
        elif num > highest3:
            highest3 = num

    return [highest1, highest2, highest3]