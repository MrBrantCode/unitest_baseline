"""
QUESTION:
Create a function `find_largest_numbers` that accepts a list of integers and returns a list of the largest number from each group of equal numbers, excluding any negative numbers. The function should be able to handle input numbers up to a maximum value of 10^9 and should have a time complexity of O(n log n).
"""

def find_largest_numbers(numbers):
    # Filter out negative numbers
    positive_numbers = [num for num in numbers if num >= 0]
    
    # Sort the positive numbers in descending order
    positive_numbers.sort(reverse=True)
    
    # Return the first element of each sorted sublist
    largest_numbers = [positive_numbers[i] for i in range(len(positive_numbers)) if i == 0 or positive_numbers[i] != positive_numbers[i-1]]
    
    return largest_numbers