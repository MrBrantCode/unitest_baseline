"""
QUESTION:
Write a function named `find_three_largest_numbers` that takes an array of integers as input and returns the three largest numbers in the array in descending order. The array may contain duplicate numbers and may not be sorted. The function should find the three largest numbers efficiently, and the input array can be of any size.
"""

def find_three_largest_numbers(array):
    largest_numbers = [float('-inf')] * 3  # Initialize a list of 3 largest numbers as negative infinity
    
    for num in array:
        if num > largest_numbers[0]:  # If the number is greater than the largest number
            largest_numbers[2] = largest_numbers[1]
            largest_numbers[1] = largest_numbers[0]
            largest_numbers[0] = num
        elif num > largest_numbers[1]:  # If the number is greater than the second largest number
            largest_numbers[2] = largest_numbers[1]
            largest_numbers[1] = num
        elif num > largest_numbers[2]:  # If the number is greater than the third largest number
            largest_numbers[2] = num
    
    return sorted(largest_numbers, reverse=True)