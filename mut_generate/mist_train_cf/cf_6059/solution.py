"""
QUESTION:
Write a function `count_quadruplets` that takes an array of integers as input and returns the number of quadruplets that satisfy the triangle inequality, along with the actual quadruplets. The function should have a time complexity of O(n^3) and constant space complexity. It should handle negative integers and floating-point numbers, as well as duplicates in the input array. The function should also optimize the solution by avoiding unnecessary calculations, such as not checking for permutations of the quadruplet that have the same elements but in a different order.
"""

def count_quadruplets(arr):
    """
    This function takes an array of integers as input and returns the number of quadruplets 
    that satisfy the triangle inequality, along with the actual quadruplets.

    Parameters:
    arr (list): A list of integers.

    Returns:
    tuple: A tuple containing the count of valid quadruplets and the quadruplets themselves.
    """
    
    # Sort the array in ascending order
    arr.sort()

    # Initialize count and quadruplets
    count = 0
    quadruplets = []

    # Iterate over the array
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            for k in range(j + 1, len(arr)):
                for m in range(k + 1, len(arr)):
                    # Check if the sum of the three sides is greater than the fourth side
                    if arr[i] + arr[j] + arr[k] > arr[m]:
                        count += 1
                        quadruplets.append([arr[i], arr[j], arr[k], arr[m]])

    return count, quadruplets