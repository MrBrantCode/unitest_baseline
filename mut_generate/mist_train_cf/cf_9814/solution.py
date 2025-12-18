"""
QUESTION:
Write a function `sum_and_count_distinct` that takes an array of integers as input and returns a tuple containing the sum of all integers and the count of distinct elements. The function should have a time complexity of O(n) and a space complexity of O(n).
"""

def sum_and_count_distinct(arr):
    # Create a dictionary to store the count of each distinct element
    count_dict = {}

    # Initialize the sum and count of distinct elements to zero
    sum = 0
    count = 0

    # Iterate over the array
    for num in arr:
        # Add the current number to the sum
        sum += num

        # Check if the current number is already in the dictionary
        if num in count_dict:
            # If it is, increment its count by 1
            count_dict[num] += 1
        else:
            # If it is not, add it to the dictionary with a count of 1
            count_dict[num] = 1
            # Increment the count of distinct elements by 1
            count += 1

    # Return the sum and count of distinct elements
    return sum, count