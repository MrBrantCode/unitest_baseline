"""
QUESTION:
Write a function `find_triplets(arr)` that finds the number of unique triplets in the given array that sum up to zero. The input array may contain duplicate elements, and the function should return the count of unique triplets. The function should assume that the input array contains at least three elements.
"""

def find_triplets(arr):
    arr.sort()  # Sort the array in ascending order
    count = 0  # Count of unique triplets
    
    for i in range(len(arr) - 2):  # Iterate through each element except the last two
        if i > 0 and arr[i] == arr[i-1]:
            continue  # Skip duplicates
        
        left = i + 1  # Left pointer
        right = len(arr) - 1  # Right pointer
        
        while left < right:
            triplet_sum = arr[i] + arr[left] + arr[right]
            
            if triplet_sum == 0:
                count += 1
                left += 1
                right -= 1
                
                while left < right and arr[left] == arr[left - 1]:
                    left += 1  # Skip duplicates
                while left < right and arr[right] == arr[right + 1]:
                    right -= 1  # Skip duplicates
                    
            elif triplet_sum < 0:
                left += 1
            else:
                right -= 1
    
    return count