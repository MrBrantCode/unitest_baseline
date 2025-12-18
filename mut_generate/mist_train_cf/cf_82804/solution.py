"""
QUESTION:
Find the kth least significant prime number in an array of numbers, considering the element at the 0th index as the 'least significant' and the element at the (n-1)th index as the 'most significant'. The function should take an array of integers and an integer k as input, and return the kth smallest prime number in the array with a computational complexity of O(n). If the array contains less than k prime numbers, return a special value to signify this.
"""

def isPrime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def kth_least_significant_prime(nums, k):
    prime_list = [num for num in nums if isPrime(num)]
    prime_list.sort()
    if len(prime_list) < k:
        return None
    return prime_list[k - 1]