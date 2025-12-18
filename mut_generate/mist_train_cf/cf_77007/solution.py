"""
QUESTION:
Write a function named `find_second_smallest` that accepts an array of floating-point numbers as input and returns the second smallest unique number in the array. The function should handle edge cases like duplicate entries, negative numbers, and zero. If the array has less than two unique numbers, the function should return "Array doesn't have enough unique numbers." The solution should be efficient and not use built-in functions to sort the array.
"""

def find_second_smallest(numbers):
    # Remove duplicate entries using set
    numbers = list(set(numbers))
    # Check if we have less than two unique numbers
    if len(numbers) < 2:
        return "Array doesn't have enough unique numbers."
    else:
        # Initialize the smallest and second smallest
        smallest = second_smallest = float('inf')
        # Go through each number in the list
        for num in numbers:
            # Update smallest if found a smaller number
            if num <= smallest:
                second_smallest = smallest
                smallest = num
            # Update second smallest if current element is greater than 
            # smallest and smaller than second smallest
            elif num < second_smallest:
                second_smallest = num
        # Return the second smallest number
        return second_smallest