"""
QUESTION:
Implement a function named `nextPrimePermutation(nums)` that rearranges the input list `nums` into the lexicographically next greater permutation of numbers. If such an arrangement is not possible, it must rearrange it as the lowest possible order (i.e., sorted in ascending order). The function should return a tuple where the first element is the rearranged list and the second element indicates whether the sum of the digits in the rearranged list is a prime number. The function must use constant extra memory and perform the replacement in place. The input list `nums` will have a length between 1 and 100, inclusive, and each element will be between 0 and 100, inclusive.
"""

def nextPrimePermutation(nums):
    n = len(nums)
    i = n - 2
    while i >= 0 and nums[i] >= nums[i+1]:
        i -= 1

    if i >= 0:
        j = n - 1
        while j > i and nums[j] <= nums[i]:
            j -= 1
        nums[i], nums[j] = nums[j], nums[i]

    left, right = i + 1, n - 1
    while left < right:
        nums[left], nums[right] = nums[right], nums[left]
        left += 1
        right -= 1

    def isPrime(n):
        if n < 2:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        p = 3
        while p * p <= n:
            if n % p == 0:
                return False
            p += 2
        return True

    sum_of_digits = sum(nums)
    is_prime = isPrime(sum_of_digits)

    if not is_prime:
        nums.sort()

    return (nums, is_prime)