"""
QUESTION:
Write a function `count_zero_triplets(arr)` that takes a non-empty array of integers as input, which may contain duplicates and be of any length. The function must use the two-pointer approach and sort the array in non-decreasing order to find all unique triplets that sum up to zero. The function should return the count of such triplets. The solution should have a space complexity of O(1) and an optimized time complexity.
"""

def count_zero_triplets(arr):
    arr.sort()
    count = 0
    
    for i in range(len(arr) - 2):
        if i > 0 and arr[i] == arr[i-1]:
            continue
        
        left = i + 1
        right = len(arr) - 1
        
        while left < right:
            sum = arr[i] + arr[left] + arr[right]
            
            if sum == 0:
                count += 1
                
                while left < right and arr[left] == arr[left+1]:
                    left += 1
                
                while left < right and arr[right] == arr[right-1]:
                    right -= 1
                
                left += 1
                right -= 1
            
            elif sum < 0:
                left += 1
            else:
                right -= 1
    
    return count