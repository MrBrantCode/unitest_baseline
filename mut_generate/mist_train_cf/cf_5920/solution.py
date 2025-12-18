"""
QUESTION:
Create a function called `multiply_array` that takes an array of integers as input and returns a new array where each element is multiplied by the smallest prime number greater than 13. If any element in the input array is divisible by the smallest prime number greater than 13, replace that element with the next prime number greater than 13 before multiplying.
"""

def multiply_array(arr):
    def smallest_prime_greater_than_13():
        num = 14
        while True:
            is_prime = True
            for i in range(2, int(num**0.5) + 1):
                if num % i == 0:
                    is_prime = False
                    break
            if is_prime:
                return num
            num += 1

    smallest_prime = smallest_prime_greater_than_13()
    next_prime = smallest_prime + 1
    while not all(next_prime % i != 0 for i in range(2, int(next_prime**0.5) + 1)):
        next_prime += 1

    result = []
    for num in arr:
        if num % smallest_prime == 0:
            result.append(num * next_prime)
        else:
            result.append(num * smallest_prime)
    return result