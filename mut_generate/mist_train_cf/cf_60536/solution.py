"""
QUESTION:
Develop a function named `check_ascending` that takes a multidimensional numeric array as input and returns a tuple containing a boolean value indicating whether the elements in the array adhere to an ascending progression and the location of the first non-ascending progression if found. The function should compare elements within each subarray and across subarrays.
"""

def check_ascending(arr):
    # iterate over the subarrays
    for i in range(len(arr)):
        # iterate over the elements within a subarray
        for j in range(len(arr[i])):
            # If it's the last element in a subarray,
            if j == len(arr[i])-1:
                # skip if it's also the last subarray
                if i == len(arr)-1:
                    continue
                # compare it with the first element of the next subarray
                elif arr[i][j] > arr[i+1][0]:
                    return False, (i,j)
            # if it's not the last element, compare it with the next one
            elif arr[i][j] > arr[i][j+1]:
                return False, (i,j)
    return True, None