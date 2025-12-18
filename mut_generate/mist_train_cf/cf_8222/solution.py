"""
QUESTION:
Write a function called `sum_of_squares` that takes three integers as input and returns the sum of the squares of the two largest numbers.
"""

def sum_of_squares(num1, num2, num3):
    nums = [num1, num2, num3]  
    nums.sort()  

    sum_of_squares = (nums[1] ** 2) + (nums[2] ** 2)  
    
    return sum_of_squares