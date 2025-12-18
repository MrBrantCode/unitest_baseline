"""
QUESTION:
Given a list of integers and a target sum, find three distinct numbers in the list such that their sum equals the target sum and the numbers satisfy the following conditions: the first number is negative, the second number is prime, and the third number is zero. Return the three numbers as a list if such numbers exist, otherwise return an empty list.
"""

def find_triplet(nums, target):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    prime = []
    zero = 0
    negative = None

    for num in nums:
        if num < 0 and num != 0:
            negative = num
        elif num != 0 and is_prime(num):
            prime.append(num)
        elif num == 0:
            zero = num

    prime.sort()

    for p in prime:
        remaining = target - p
        if remaining == negative:
            return [negative, p, zero]
        elif remaining >= 0:
            break

    return []