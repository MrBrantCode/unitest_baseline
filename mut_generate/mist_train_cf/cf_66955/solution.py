"""
QUESTION:
Create a function called `add_two_numbers` that takes an array of two integers as input and returns the sum of the two numbers along with a message indicating whether the two numbers are the same or different, and whether their sum is a prime number or not. Assume the input array always contains exactly two integers.
"""

def add_two_numbers(nums):
    def is_prime(num):
        if num <= 1:
            return False
        for i in range(2, num):
            if num % i == 0:
                return False
        return True

    if nums[0] == nums[1]:
        return nums[0] + nums[1], "The numbers are the same", "The sum is a prime number" if is_prime(nums[0] + nums[1]) else "The sum is not a prime number"
    else:
        return nums[0] + nums[1], "The numbers are different", "The sum is a prime number" if is_prime(nums[0] + nums[1]) else "The sum is not a prime number"