"""
QUESTION:
Design a function called `arrange_array` that rearranges an array of integers such that all odd numbers come before even numbers. The function should have a time complexity of O(n), where n is the length of the array, and should not modify the relative order of the numbers within each category. The function should also handle negative numbers correctly, arranging them in the same order as positive numbers. The function should not use any extra space.
"""

def arrange_array(arr):
    left, right = 0, len(arr) - 1  

    while left < right:  
        if arr[left] % 2 == 0 and arr[right] % 2 == 1:  
            arr[left], arr[right] = arr[right], arr[left]  
            left += 1  
            right -= 1

        if arr[left] % 2 == 1:  
            left += 1  

        if arr[right] % 2 == 0:  
            right -= 1  

    return arr