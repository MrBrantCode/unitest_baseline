"""
QUESTION:
Write a function `remove_primes` that takes an array of integers as input and removes all prime numbers from the array in-place. The function should iterate over the array in reverse order and should not use any built-in array manipulation functions or create a new array to store the result. The time complexity of the function should be O(n), where n is the length of the array.
"""

def remove_primes(nums):
    def is_prime(num):
        if num <= 1:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    write_idx = 0
    for read_idx in range(len(nums)):
        if not is_prime(nums[read_idx]):
            nums[write_idx] = nums[read_idx]
            write_idx += 1

    # update the length of the array by removing the extra elements
    del nums[write_idx:]