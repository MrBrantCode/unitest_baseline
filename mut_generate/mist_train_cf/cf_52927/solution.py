"""
QUESTION:
Design a function `longest_sublist(nums)` that takes a list of integers `nums` as input and returns the starting and ending indices of the longest continuous sublist containing both prime and composite numbers. The function should return `None` if no such sublist exists.
"""

def longest_sublist(nums):
    def is_prime(n):
        if n <= 1: return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    prime, compo = False, False
    curr_start, start, end = 0, 0, 0
    max_len = 0  
    for i, num in enumerate(nums):
        if is_prime(num):
            prime = True
        else:
            compo = True
        if prime and compo and i - curr_start + 1 > max_len:
            max_len = i - curr_start + 1
            start, end = curr_start, i
        elif i != len(nums)-1 and ((is_prime(num) and not is_prime(nums[i+1]))
                                   or (not is_prime(num) and is_prime(nums[i+1]))):
            prime, compo = False, False
            curr_start = i + 1
    return (start, end) if max_len > 0 else None