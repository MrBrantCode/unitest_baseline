"""
QUESTION:
Create a function `get_sorted_primes` that takes a list of integers as input, filters out non-prime numbers, removes duplicates, and returns a new list sorted in descending order. The function must not use any built-in sorting or duplicate removal functions. The input list can contain up to 1 million elements.
"""

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def get_sorted_primes(nums):
    # Filter out non-prime numbers
    prime_list = [x for x in nums if is_prime(x)]
    
    # Implement custom sorting algorithm (bubble sort in this case)
    for i in range(len(prime_list)):
        for j in range(len(prime_list) - 1):
            if prime_list[j] < prime_list[j + 1]:
                prime_list[j], prime_list[j + 1] = prime_list[j + 1], prime_list[j]
                
    # Remove duplicates
    final_list = []
    for x in prime_list:
        if x not in final_list:
            final_list.append(x)
            
    return final_list