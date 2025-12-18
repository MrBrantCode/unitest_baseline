"""
QUESTION:
Write a function named `find_quadruplets` that takes a numerical array `arr` and an integer `total` as parameters. This function should return the count of unique quadruplets in the array whose sum equals the given total and the quadruplets themselves. A quadruplet is considered unique if it does not contain the same elements in a different order. The function should be implemented without using any pre-established libraries or subroutines and should be optimized to handle large input arrays efficiently.
"""

def find_quadruplets(arr, total):
    quadruplets = set()
    
    # Sort the array to decrease the search time
    arr.sort()

    for i in range(len(arr)-3):
        for j in range(i+1, len(arr)-2):
            left = j+1
            right = len(arr)-1
            
            while left < right:
                current_sum = arr[i] + arr[j] + arr[left] + arr[right]
                
                if current_sum == total:
                    # Found a quadruplet, add to set
                    quadruplets.add((arr[i], arr[j], arr[left], arr[right]))

                    # Remove elements with the same value from left to avoid duplicate quadruplets
                    while left < right and arr[left] == arr[left+1]:
                        left += 1

                    # Remove elements with the same value from right to avoid duplicate quadruplets
                    while left < right and arr[right] == arr[right-1]:
                        right -= 1

                    left += 1
                    right -= 1
                
                elif current_sum < total:
                    # Current sum is too small, move left pointer to right to increase it
                    left += 1
                
                else:
                    # Current sum is too big, move right pointer to left to decrease it
                    right -= 1

    # Convert the set of quadruplets to a list and return it along with the count of quadruplets
    return len(quadruplets), list(map(list, quadruplets))