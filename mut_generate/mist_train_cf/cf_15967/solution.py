"""
QUESTION:
Write a function `find_largest_numbers` that takes a list of integers as input, filters out negative numbers, and returns a list of the largest number from each group of equal values. The function should handle input numbers up to a maximum value of 10^9 and have a time complexity of O(n log n).
"""

def find_largest_numbers(numbers):
    # Filter out negative numbers
    positive_numbers = [num for num in numbers if num >= 0]
    
    # Sort the positive numbers in descending order
    positive_numbers.sort(reverse=True)
    
    # Return the first element of each sorted sublist
    largest_numbers = [positive_numbers[i] for i in range(len(positive_numbers)) if i == 0 or positive_numbers[i] != positive_numbers[i-1]]
    
    return largest_numbers