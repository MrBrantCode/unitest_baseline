"""
QUESTION:
Implement a function named `calculateMinimumDifference` that calculates the smallest non-zero absolute difference between any two numbers in a list of numbers. The input list should contain more than one integer. The function should handle potential errors such as non-integer inputs, non-list inputs, and lists with less than two unique integers. If an error occurs, the function should return a descriptive error message.
"""

def calculateMinimumDifference(nums):
    try:
        # Check if the list has more than one element
        if len(nums) <= 1: 
            return "Error: The input list should contain more than one integer."

        # Check for non-integer entries
        if not all(isinstance(x, int) for x in nums):
            return "Error: Invalid input. Numbers are expected."

        # Calculate the absolute difference between each pair of numbers
        diffs = [abs(nums[x] - nums[x-1]) for x in range(1, len(nums))]

        # Find the smallest non-zero difference
        min_diff = min(x for x in diffs if x != 0)
        return min_diff

    except TypeError:
        return "Error: Invalid input. Please enter a list of numbers."
    except ValueError:
        return "Error: Invalid input. The list should contain more than one unique integer value."