"""
QUESTION:
Create a function `create_buckets` that takes a list of integers as input and returns a list of lists of integers, where each sublist represents a bucket. The function must adhere to the following conditions:
- Each bucket must contain at least three elements.
- The sum of the elements in each bucket must be a prime number.
- Each bucket should be sorted in ascending order.
"""

def is_prime(n):
    """Check if a number is prime."""
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def create_buckets(nums):
    """Create buckets of integers with a prime sum."""
    nums.sort()
    buckets = []
    for num in nums:
        added = False
        for bucket in buckets:
            if len(bucket) < 3 and is_prime(sum(bucket) + num):
                bucket.append(num)
                added = True
                break
        if not added:
            buckets.append([num])
    buckets = [bucket for bucket in buckets if len(bucket) >= 3]
    return [sorted(bucket) for bucket in buckets]