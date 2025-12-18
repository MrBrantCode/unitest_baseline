"""
QUESTION:
Create a function named `list_primes` that takes a list of integers as input and returns a list of prime numbers from the input list. The function should handle non-numerical entries in the list and potential exceptions, and estimate its time complexity. The function should also return the time taken to execute.
"""

import time

def list_primes(num_list):
    try:
        if num_list == []:
          return("The list has no numbers.")
        start_time = time.time()
        primes = [num for num in num_list if type(num) == int and num > 1 and all(num%i!=0 for i in range(2,num))]
        end_time = time.time() - start_time
        return(primes, end_time)
    except TypeError as e:
        return (str(e))