"""
QUESTION:
Create a function `find_prime_indices` that takes a list of integers as input and returns the indices of the largest and second largest prime numbers in the list. The function should handle negative integers as non-prime numbers, and should not use any additional data structures or built-in prime-checking functions. The function should have a time complexity of O(n^2 log n), where n is the size of the list. If no prime numbers are found, the function should return -1 for the indices of both the largest and second largest prime numbers.
"""

def find_prime_indices(nums):
    largest_index = -1
    second_largest_index = -1

    for i, num in enumerate(nums):
        if num < 0:
            continue

        is_prime = True
        if num < 2:
            is_prime = False
        else:
            for j in range(2, int(num ** 0.5) + 1):
                if num % j == 0:
                    is_prime = False
                    break

        if is_prime:
            if largest_index == -1 or num > nums[largest_index]:
                second_largest_index = largest_index
                largest_index = i
            elif second_largest_index == -1 or num > nums[second_largest_index]:
                second_largest_index = i

    return largest_index, second_largest_index