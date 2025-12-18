"""
QUESTION:
Find the count of unique triplets in a given array that sum up to zero. 

The input array can have duplicates and be of any length. The solution should have a space complexity of O(1) and optimized time complexity. Implement the function `find_triplets(arr)` to take the array as input and return the count of unique triplets that sum up to zero.
"""

def find_triplets(arr):
    n = len(arr)
    arr.sort()
    count = 0

    for i in range(n-2):
        if i > 0 and arr[i] == arr[i-1]:
            continue

        left = i + 1
        right = n - 1

        while left < right:
            if arr[i] + arr[left] + arr[right] == 0:
                count += 1
                left += 1
                right -= 1

                while left < right and arr[left] == arr[left-1]:
                    left += 1
                while left < right and arr[right] == arr[right+1]:
                    right -= 1

            elif arr[i] + arr[left] + arr[right] < 0:
                left += 1
            else:
                right -= 1

    return count