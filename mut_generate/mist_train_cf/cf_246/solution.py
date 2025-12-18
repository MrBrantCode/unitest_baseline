"""
QUESTION:
Write a function `is_prime_binary_search` that takes a sorted list of integers as input and prints all prime numbers in the list using a binary search algorithm. The function should implement a helper function `is_prime` to check if a number is prime. The binary search should start from the first element of the list and move towards the end, printing each prime number as it is found.
"""

def is_prime_binary_search(sorted_list):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    low = 0
    high = len(sorted_list) - 1

    while low <= high:
        mid = (low + high) // 2
        if is_prime(sorted_list[mid]):
            print(sorted_list[mid])
            low = mid + 1
        else:
            high = mid - 1