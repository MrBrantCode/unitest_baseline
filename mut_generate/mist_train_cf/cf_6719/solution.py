"""
QUESTION:
Write a function `largest_adjacent_prime_sum` that finds two adjacent prime numbers in an array with the largest sum greater than a given threshold value. The two adjacent prime numbers must not be located at the beginning or end of the array.
"""

def largest_adjacent_prime_sum(arr, threshold):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    max_sum = 0
    for i in range(1, len(arr) - 1):
        if is_prime(arr[i]) and is_prime(arr[i+1]):
            max_sum = max(max_sum, arr[i] + arr[i+1])

    return max_sum if max_sum > threshold else -1