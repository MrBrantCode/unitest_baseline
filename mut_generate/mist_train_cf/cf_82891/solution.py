"""
QUESTION:
Implement a function `threeSum(arr, targetSum)` that returns all unique triplets in the given array `arr` whose elements sum up exactly to `targetSum`, with the following constraints:

*   Each number in the array can only be used once.
*   The resulting triplets should be sorted by their first elements, and for tie-breaking, they should be sorted by the second elements.
*   The output should be sorted in ascending order.
*   The time complexity should be less than or equal to O(n^2).
"""

def threeSum(arr, targetSum):
    arr.sort()  
    result = []
    for i in range(len(arr) - 2):         
        if i > 0 and arr[i] == arr[i - 1]:  
            continue
        new_target = targetSum - arr[i]  
        left, right = i + 1, len(arr) - 1
        while left < right:
            if arr[left] + arr[right] == new_target:  
                result.append([arr[i], arr[left], arr[right]])
                left += 1
                while left < right and arr[left] == arr[left - 1]:  
                    left += 1
            elif arr[left] + arr[right] < new_target:  
                left += 1
            else:  
                right -= 1
    return result