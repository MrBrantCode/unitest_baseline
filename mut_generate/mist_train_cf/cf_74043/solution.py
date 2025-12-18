"""
QUESTION:
Write a function `findPairs(nums, k)` that takes an array of integers `nums` and an integer `k` as input, and returns two values: the number of unique k-diff pairs in the array, and the number of unique k-diff pairs where the sum of the pair is a prime number.

A k-diff pair is an integer pair `(nums[i], nums[j])`, where `0 <= i, j < nums.length`, `i != j`, and `|nums[i] - nums[j]| == k`. A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself.

The function should have a time complexity of O(n) and a space complexity of O(n), where n is the length of the array.

Constraints: `1 <= nums.length <= 10^4`, `-10^7 <= nums[i] <= 10^7`, and `0 <= k <= 10^7`. If `k < 0`, the function should return `(0, 0)`.
"""

def findPairs(nums, k):
    """
    Returns the number of unique k-diff pairs in the array and the number of unique k-diff pairs where the sum of the pair is a prime number.

    Args:
        nums (list): A list of integers.
        k (int): The difference between pairs.

    Returns:
        tuple: A tuple containing the number of unique k-diff pairs and the number of unique k-diff pairs with a prime sum.
    """
    if k < 0:
        return 0, 0

    def is_prime(n):
        """Checks if a number is prime."""
        if n <= 1:
            return False
        if n == 2:
            return True
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    num_map, res, prime_count = {}, 0, 0
    for num in nums:
        num_map[num] = num_map.get(num, 0) + 1

    for key in num_map:
        if k == 0:
            if num_map[key] > 1:
                res += 1
        else:
            if key + k in num_map:
                res += 1
            if key + k in num_map and is_prime(key + key + k):
                prime_count += 1

    return res, prime_count