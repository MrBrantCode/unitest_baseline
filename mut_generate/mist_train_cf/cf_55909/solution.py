"""
QUESTION:
Design an efficient algorithm to compute the greatest common divisor (GCD) of an array of at least 5 numbers, with a performance time constraint. The algorithm should be able to handle large inputs. Implement a function named `compute_gcd_array` that takes an array of integers as input and returns the GCD of all the numbers in the array. The function should use the Euclidean algorithm to compute the GCD of two numbers.
"""

def compute_gcd_array(numbers):
    def gcd(x, y):
        while(y):
            x, y = y, x % y
        return x
    
    num1 = numbers[0]
    num2 = numbers[1]
    gcd_num = gcd(num1, num2)
 
    for i in range(2, len(numbers)):
        gcd_num = gcd(gcd_num, numbers[i])
     
    return gcd_num