"""
QUESTION:
Write a function `sum_of_primes_3D_array` that takes a 3D array of integers as input and returns the sum of all prime numbers existing in each sub-array.
"""

def sum_of_primes_3D_array(arr):
    def is_prime(num):
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    return False
            else:
                return True
        else:
            return False
            
    total_sum = 0
    for sub_arr in arr:
        for sub_sub_arr in sub_arr:
            for item in sub_sub_arr:
                if is_prime(item):
                    total_sum += item
    return total_sum