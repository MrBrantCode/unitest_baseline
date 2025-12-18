"""
QUESTION:
Create a function `rotate_list(nums, k)` that rotates the elements in the list `nums` by `k` times to the right, where `k` is a prime number. If `k` is not a prime number, return the error message "Error: The number of times to rotate must be a prime number." The rotation should be done in-place or with minimal extra space.
"""

def rotate_list(nums, k):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    if not is_prime(k):
        return "Error: The number of times to rotate must be a prime number."
    
    n = len(nums)
    k %= n
    
    return nums[-k:] + nums[:-k]