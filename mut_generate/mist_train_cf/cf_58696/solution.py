"""
QUESTION:
Write a function called `find_first_prime` that takes a list of elements as input and returns the first prime number found in the list. The function should skip non-integer values and consider only integers greater than 1. If no prime number is found in the list, the function should return `None`.
"""

def find_first_prime(lst):
    for num in lst:
        if isinstance(num, int) and num > 1:  
            for i in range(2, num):
                if (num % i) == 0:  
                    break
            else:  
                return num
    return None  