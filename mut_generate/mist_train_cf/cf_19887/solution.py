"""
QUESTION:
Write a function named `kth_smallest_prime` that takes a list of positive integers and an integer `k` as inputs. The function should return the kth smallest prime number from the list, considering only unique numbers and ignoring non-prime numbers. If `k` is greater than the number of prime numbers in the list, the function should return `None`.
"""

def kth_smallest_prime(lst, k):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    unique_nums = list(set(lst))
    primes = [num for num in unique_nums if is_prime(num)]
    sorted_primes = sorted(primes)
    
    return sorted_primes[k - 1] if k <= len(sorted_primes) else None