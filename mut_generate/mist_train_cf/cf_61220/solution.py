"""
QUESTION:
Write a function `maxAscendingSum(nums)` that takes an array of positive integers `nums` as input, where `1 <= nums.length <= 1000` and `1 <= nums[i] <= 1000`, and returns the maximum possible sum of an ascending subarray in `nums` that contains at least one prime number. If there are multiple subarrays with the same maximum sum, return the one with the smallest length. If there is still a tie, return the one that appears first. If no such subarray exists, return -1.
"""

def maxAscendingSum(nums):
    def isPrime(n):
        if n <= 1:
            return False
        if n <= 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True

    max_sum = 0
    curr_sum = nums[0]
    prime_exists = isPrime(nums[0])
    max_len = float('inf')
    curr_len = 1

    for idx in range(1, len(nums)):
        if nums[idx] > nums[idx-1] and nums[idx] not in nums[max_sum:idx]:
            curr_sum += nums[idx]
            curr_len += 1
            if not prime_exists:
                prime_exists = isPrime(nums[idx])
        else:
            if curr_sum > max_sum and prime_exists:
                if curr_sum == max_sum:
                    max_len = min(max_len, curr_len)
                else:
                    max_sum = curr_sum
                    max_len = curr_len
            elif curr_sum == max_sum and prime_exists and curr_len < max_len:
                max_len = curr_len
            curr_sum = nums[idx]
            prime_exists = isPrime(nums[idx])
            curr_len = 1

    if curr_sum > max_sum and prime_exists:
        max_sum = curr_sum
    elif curr_sum == max_sum and prime_exists and curr_len < max_len:
        max_sum = curr_sum

    return max_sum if max_sum != 0 else -1