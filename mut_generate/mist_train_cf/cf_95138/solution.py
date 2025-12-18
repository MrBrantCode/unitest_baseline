"""
QUESTION:
Create a function named `find_all_sums` that takes an array of integers as input, including negative numbers. The function should return a list of all possible sums of two numbers in the array, in descending order, without using any built-in functions or libraries for summation or sorting.
"""

def find_all_sums(arr):
    # Create a list to store all the sums
    sums = []

    # Iterate through each pair of numbers in the array
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            # Calculate the sum of the pair
            pair_sum = arr[i] + arr[j]
            
            # Add the sum to the list of sums
            sums.append(pair_sum)

    # Sort the list of sums in descending order using bubble sort algorithm
    for i in range(len(sums) - 1):
        for j in range(len(sums) - 1 - i):
            if sums[j] < sums[j + 1]:
                sums[j], sums[j + 1] = sums[j + 1], sums[j]

    # Return the list of sums
    return sums