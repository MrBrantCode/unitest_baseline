"""
QUESTION:
Construct a function `max_positive_whole_number` that takes an array of integers as input and returns the maximum positive whole number that can be formed by concatenating the digits of the positive numbers in the array. The function should ignore negative numbers in the array. The function should return the maximum possible whole number, treating each integer as a separate digit. If no positive numbers are present in the array, the function can return `None`.
"""

def max_positive_whole_number(nums):
    # Filter out the negative numbers from the array
    filtered_nums = filter(lambda x: x > 0, nums)
  
    # Convert the numbers to string and sort them in descending order
    str_nums = sorted(map(str, filtered_nums), reverse=True)
  
    # Join the string numbers
    joined_str = ''.join(str_nums)
  
    # Return None if no positive number is found, otherwise convert the string back to an integer
    return int(joined_str) if joined_str else None