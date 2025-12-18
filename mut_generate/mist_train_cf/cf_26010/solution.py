"""
QUESTION:
Write a function `isArmstrong(num)` to check if a given number is an Armstrong number. An Armstrong number is a number when the sum of the nth power of its own digits is equal to the number itself, where n is the number of digits. The function should return True if the number is an Armstrong number, False otherwise.
"""

def is_armstrong(num):
    # obtain number of digits 
    digits = len(str(num))

    # initialize sum
    total_sum = 0

    # find sum of nth power of digits 
    temp = num 
    while temp > 0:
        digit = temp % 10
        total_sum = total_sum + digit ** digits
        temp //= 10

    # return true or false
    return total_sum == num