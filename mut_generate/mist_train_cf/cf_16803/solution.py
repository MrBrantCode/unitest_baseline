"""
QUESTION:
Create a function called "print_perfect_numbers" that takes in an integer "n" and prints all perfect numbers between 1 and "n". A perfect number is a positive integer that is equal to the sum of its proper divisors, excluding itself. Proper divisors are the positive divisors of a number, excluding the number itself. The function should return the list of perfect numbers found.
"""

def print_perfect_numbers(n):
    """Prints all perfect numbers between 1 and 'n'."""
    
    perfect_numbers = []
    
    for num in range(1, n+1):
        divisors = []
        
        for i in range(1, num):
            if num % i == 0:
                divisors.append(i)
        
        sum_divisors = sum(divisors)
        
        if num == sum_divisors:
            perfect_numbers.append(num)
    
    return perfect_numbers