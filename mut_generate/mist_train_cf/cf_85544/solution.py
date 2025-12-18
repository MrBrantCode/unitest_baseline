"""
QUESTION:
Create a function named `sort_and_count_primes` that takes a list of integers as input. The function should sort the input list in ascending order and count the number of prime numbers in the list. Return the sorted list and the count of prime numbers. Note that the function should be efficient for smaller lists, but may not be optimal for large lists due to the prime checking algorithm's time complexity.
"""

def sort_and_count_primes(list_nums):
    def is_prime(num):
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    return False
            else:
                return True
        return False

    sorted_list = sorted(list_nums)
    prime_numbers = [num for num in sorted_list if is_prime(num)]
    return sorted_list, len(prime_numbers)