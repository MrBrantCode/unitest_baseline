"""
QUESTION:
Write a function named `calculate_sum` that calculates the sum of even and odd numbers separately from a list of integers, with a time complexity of O(n), where n is the size of the input data. The function should handle positive and negative odd numbers differently, adding positive odd numbers and negative odd numbers that are divisible by 3 to the sum of odd numbers, and other negative odd numbers to the sum of even numbers.
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