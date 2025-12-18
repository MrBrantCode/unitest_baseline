"""
QUESTION:
Implement a function `find_triplets(arr, target)` that finds all unique sets of three distinct numbers in a given array `arr` that sum up to a given number `target`. The array `arr` will contain positive integers only and can have duplicate values. The function should return the triplets in ascending order, without any duplicates.
"""

def find_triplets(arr, target):
    # Sort the array in ascending order
    arr.sort()
    n = len(arr)
    triplets = []
    
    # Iterate through the array
    for i in range(n-2):
        # Skip duplicates
        if i > 0 and arr[i] == arr[i-1]:
            continue
        left = i+1
        right = n-1
        while left < right:
            curr_sum = arr[i] + arr[left] + arr[right]
            if curr_sum == target:
                triplets.append([arr[i], arr[left], arr[right]])
                left += 1
                right -= 1
                # Skip duplicates
                while left < right and arr[left] == arr[left-1]:
                    left += 1
                while left < right and arr[right] == arr[right+1]:
                    right -= 1
            elif curr_sum < target:
                left += 1
            else:
                right -= 1
    return triplets