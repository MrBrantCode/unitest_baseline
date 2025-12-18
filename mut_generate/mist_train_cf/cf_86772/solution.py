"""
QUESTION:
Create a function named `sort_descending_primes` that takes a list of integers as input. The function should return a list with the input numbers in descending order, duplicates removed, and "Prime" appended after each prime number. The input list should not exceed 1000 elements, and the numbers should be between -1000 and 1000. The function should run in O(nlogn) time complexity.
"""

def sort_descending_primes(nums):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    sorted_list = list(set(nums))
    sorted_list.sort(reverse=True)

    output_list = []
    for num in sorted_list:
        if is_prime(num):
            output_list.append(num)
            output_list.append("Prime")
        else:
            output_list.append(num)

    return output_list