"""
QUESTION:
Write a function named `calculate_sum` that takes a list of integers as input and returns two sums: the sum of even numbers and the sum of odd numbers. The function should handle both positive and negative numbers. If an odd number is negative and not divisible by 3, it should be added to the sum of even numbers instead. The function should have a time complexity of O(n), where n is the size of the input list.
"""

def calculate_sum(numbers):
    sum_even = 0
    sum_odd = 0
    
    for num in numbers:
        if num % 2 == 0:  
            sum_even += num
        else:  
            if num > 0:  
                sum_odd += num
            else:  
                if num % 3 == 0:  
                    sum_odd += num
                else:
                    sum_even += num
    
    return sum_even, sum_odd