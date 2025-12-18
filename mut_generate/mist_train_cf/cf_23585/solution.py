"""
QUESTION:
Create a function named `isArmstrongNumber` that determines whether a given number is an Armstrong number. An Armstrong number is a number that is equal to the sum of cubes of its digits. For example, 371 is an Armstrong number since 3*3*3 + 7*7*7 + 1*1*1 = 371. The function should return True if the number is an Armstrong number and False otherwise. Note that the input number can be any non-negative integer.
"""

def isArmstrongNumber(num):  
    sum_times_powers = 0
    temp = num
  
    while (temp != 0):  
        remainder = temp % 10 
        sum_times_powers += remainder ** 3 
        temp //= 10
  
    return sum_times_powers == num