"""
QUESTION:
Create a function `cumulative_sum` that takes an array of numbers as input and returns the cumulative sum of the elements in the array. The function should return a new array where each value is the sum of all numbers up to that position in the original array. The input array is not empty and contains only numbers.
"""

def cumulative_sum(array):
    # Create an empty list to store the cumulative sum
    cum_sum = [0] * len(array)
    
    # Initialize the first value
    cum_sum[0] = array[0]

    # Iterate over the rest of the array
    for i in range(1, len(array)):
        # Add the current number to the cumulative sum
        cum_sum[i] = cum_sum[i - 1] + array[i]
    
    # Return the resulting array
    return cum_sum