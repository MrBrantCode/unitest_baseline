"""
QUESTION:
Write a function `find_triplet_sum(arr, target)` that takes an array of integers and a target integer as input. The function should return True if there exist three distinct elements in the array whose sum is equal to the target, and False otherwise. The array may contain duplicate numbers, but the three elements selected for the sum must be different. The array may also contain negative numbers. The function should have a time complexity of at least O(n^2) and should not use any additional data structures such as sets, maps, or lists beyond the input array.
"""

def find_triplet_sum(arr, target):
    arr.sort()
    
    for i in range(len(arr)):
        left = i + 1
        right = len(arr) - 1
        
        while left < right:
            triplet_sum = arr[i] + arr[left] + arr[right]
            
            if triplet_sum == target:
                return True
            elif triplet_sum < target:
                left += 1
            else:
                right -= 1
    
    return False