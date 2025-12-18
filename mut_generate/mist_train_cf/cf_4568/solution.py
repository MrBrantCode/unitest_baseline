"""
QUESTION:
Write a function called `find_distinct_pairs` that takes an array of integers `arr` and a target number `k` as input, and returns `True` if exactly two distinct pairs of numbers in the array add up to `k`, and `False` otherwise. Each pair of numbers must consist of one positive number and one negative number, and the positive number must be greater than the negative number. The function should be efficient and scalable.
"""

def find_distinct_pairs(arr, k):
    # Create a dictionary to store the count of each number in the array
    num_count = {}
    
    # Iterate over the array and count the occurrences of each number
    for num in arr:
        num_count[num] = num_count.get(num, 0) + 1
    
    # Initialize a count variable to keep track of the number of distinct pairs found
    count = 0
    
    # Iterate over the array and check if there is a pair of numbers that adds up to k
    for num in arr:
        # Check if the current number is negative and there is a corresponding positive number that adds up to k
        if num < 0 and k - num in num_count and k - num > num:
            # If the pair is found, increment the count
            count += 1
            
            # If we have found exactly two distinct pairs, return True
            if count == 2:
                return True
    
    # If we reach this point, it means we haven't found exactly two distinct pairs
    return False