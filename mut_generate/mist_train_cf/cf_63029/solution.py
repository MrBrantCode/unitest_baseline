"""
QUESTION:
Design a function called `find_kth_prime` that takes two parameters: an array of integers and a positive integer `k`. The function should return the kth distinct prime number in the array. If there are less than `k` distinct prime numbers in the array, return a message indicating that.
"""

def find_kth_prime(lst, k):
    def is_prime(n):
        # Function to check if a number is a prime
        if n == 1 or n == 0:
            return False
        for i in range(2, int(n**0.5)+1):
            if n % i == 0:
                return False
        return True

    prime_list = [i for i in lst if is_prime(i)]
    if k <= len(prime_list):
        return sorted(set(prime_list))[k-1]
    return "There are less than k prime numbers in the list"