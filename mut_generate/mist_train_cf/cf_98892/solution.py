"""
QUESTION:
Develop a function `find_largest_sum` that takes a list of integers as input, excludes negative numbers, and returns the three numbers with the largest sum. The time complexity of the function should be O(n^3) or better.
"""

def find_largest_sum(numbers):
    # Remove negative numbers from the list
    numbers = [num for num in numbers if num >= 0]
    # Sort the list in descending order
    numbers.sort(reverse=True)
    # Initialize variables to store the three largest numbers and their sum
    largest_sum = 0
    largest_numbers = []
    # Iterate over all possible combinations of three numbers in the list
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            for k in range(j+1, len(numbers)):
                # Calculate the sum of the current three numbers
                current_sum = numbers[i] + numbers[j] + numbers[k]
                # Update the largest sum and numbers if the current sum is larger
                if current_sum > largest_sum:
                    largest_sum = current_sum
                    largest_numbers = [numbers[i], numbers[j], numbers[k]]
    return largest_numbers