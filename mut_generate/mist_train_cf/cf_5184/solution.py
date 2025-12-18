"""
QUESTION:
Write a function named `count_zero_triplets` that takes a list of integers as input and returns the count of unique triplets that sum up to zero. The function should sort the input list in non-decreasing order and use a two-pointer approach to find the triplets, with the pointers starting from the two ends of the list and moving towards each other. The function should skip duplicate triplets and have a space complexity of O(1) and an optimized time complexity. The input list can have duplicates and can be of any length.
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