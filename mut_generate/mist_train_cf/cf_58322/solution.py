"""
QUESTION:
Create a function called `process_array` that accepts an array of integers. The function should output both the original array and its reverse, without using any built-in reverse functions. Additionally, the function should count and output the number of prime numbers present in the array.
"""

def process_array(arr):
    # output the original array
    print("Original array:", arr)
    
    # reverse the array
    reversed_arr = arr[::-1]
    print("Reversed array:", reversed_arr)

    # count the number of primes
    def is_prime(num):
        if num <= 1:
            return False
        for i in range(2, num):
            if (num % i) == 0:
                return False
        return True
    prime_count = sum(is_prime(i) for i in arr)
    print("Number of primes:", prime_count)