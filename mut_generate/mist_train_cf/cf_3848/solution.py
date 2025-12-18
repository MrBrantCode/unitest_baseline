"""
QUESTION:
Create a function named `apply_function` that takes three parameters: an array of integers, a function to apply to the elements, and a number to check divisibility by. The function should return a new array containing the result of applying the given function to each element in the original array that meets the following conditions: the element is a prime number, the element is greater than the average value of all elements in the array, and the element is divisible by the given number.
"""

def apply_function(arr, func, divisible_by):
    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    avg = sum(arr) / len(arr)
    result = []
    for num in arr:
        if is_prime(num) and num > avg and num % divisible_by == 0:
            result.append(func(num))
    return result