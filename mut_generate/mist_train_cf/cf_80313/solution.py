"""
QUESTION:
Implement a function `count_unique_duos` that takes an array of numbers and a target sum as input. The function should return the count of unique pairs of numbers in the array whose sum equals the target sum. The pairs should be non-repetitive, meaning (a, b) is considered the same as (b, a). The function should not use any built-in sorting or searching subroutines or libraries.
"""

def count_unique_duos(arr, total):
    arr.sort()
    left, right = 0, len(arr) - 1
    count = 0
    while left < right:
        current_sum = arr[left] + arr[right]
        if current_sum == total:
            count += 1
            while left < right and arr[left] == arr[left + 1]: 
                left += 1    
            while left < right and arr[right] == arr[right - 1]: 
                right -= 1
            left += 1
            right -= 1
        elif current_sum < total:
            left += 1
        else:
            right -= 1
    return count