"""
QUESTION:
Write a function `prime_number_operations(arr1, arr2, arr3)` that takes three arrays `arr1`, `arr2`, and `arr3` as input, classifies each array element as either a prime number or not a prime number, and then sorts the prime numbers based on the sum of their divisors in descending order. The function should not use any built-in functions or libraries to check for prime numbers, should not use any additional data structures to store intermediate results, and should handle edge cases such as empty arrays or arrays with negative numbers. The function should have a time complexity of O(n^2) or better and should be able to handle large inputs with a maximum array size of 10^6 elements.
"""

def prime_number_operations(arr1, arr2, arr3):
    prime_numbers = []
    
    # Iterate through each element of the arrays
    for num in arr1 + arr2 + arr3:
        if num < 2:
            continue
        
        is_prime = True
        
        # Check if the number is prime
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        
        # Classify the number as prime or not prime
        if is_prime:
            prime_numbers.append(num)
    
    # Sort the prime numbers based on the sum of their divisors in descending order
    prime_numbers.sort(key=lambda x: sum(d for d in range(1, x+1) if x % d == 0), reverse=True)
    
    return prime_numbers