"""
QUESTION:
Write a function `check_square_sum` that takes an array of integers as input. The function should return a list of numbers from the input array that can be expressed as the sum of two perfect square numbers.
"""

def check_square_sum(arr):
    # Create a list for storing the results
    results = []

    # Go through every number in the array
    for num in arr:
        # Go through every possible pair of numbers
        for i in range(int(num ** 0.5) + 1):
            for j in range(i ,int(num ** 0.5) + 1):
                # If the sum of the squares equals the number, add it to the results
                if i ** 2 + j ** 2 == num:
                    results.append(num)
                    break  # No need to check other pairs
            else: continue  # Only executed if the inner loop did NOT break
            break  # Inner loop was broken, break the outer.

    # Return the results
    return results