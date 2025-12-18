"""
QUESTION:
Create a function named `find_all_sums` that takes an array of integers as input and returns all possible sums of two distinct numbers in the array. The function should handle negative numbers, return the sums in descending order, and have a time complexity of O(n^2). Do not use any built-in functions or libraries for summation or sorting.
"""

def find_all_sums(arr):
    # Initialize a list to store the sums
    sums = []

    # Loop through each pair of distinct numbers in the array
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            # Calculate the sum of the two numbers
            sum = arr[i] + arr[j]
            
            # Add the sum to the list of sums
            sums.append(sum)

    # Sort the list of sums in descending order
    for i in range(len(sums)):
        for j in range(i+1, len(sums)):
            if sums[i] < sums[j]:
                sums[i], sums[j] = sums[j], sums[i]

    # Return the sorted list of sums
    return sums