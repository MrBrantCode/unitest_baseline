"""
QUESTION:
Write a function `generate_array` that generates an array of unique numbers from 0 to 100 in increasing order, where the sum of all numbers in the array is a prime number, the number of odd numbers in the array is a perfect square, and the number of even numbers in the array is a Fibonacci number. The function must run in O(n) time complexity and O(1) space complexity.
"""

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def generate_array():
    array = []
    n = 0
    num_odd = 0
    num_even = 0

    for i in range(101):
        if i % 2 == 0:
            num_even += 1
        else:
            num_odd += 1

        array.append(i)
        n += i

        # Check if the sum is prime
        if is_prime(n):
            # Check if the number of odd numbers is a perfect square
            if int(num_odd**0.5)**2 == num_odd:
                # Check if the number of even numbers is a Fibonacci number
                a, b = 0, 1
                while b <= num_even:
                    if b == num_even:
                        return array
                    a, b = b, a + b

    return None