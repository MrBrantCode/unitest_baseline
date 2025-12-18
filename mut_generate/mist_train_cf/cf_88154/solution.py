"""
QUESTION:
Create a function named `prime_number_operations` that takes in three integer arrays as input: `arr1`, `arr2`, and `arr3`. Classify each array element as either prime numbers or not prime numbers, then for each prime number, find the sum of all its divisors. Finally, sort the prime numbers based on the sum of their divisors in descending order. The solution should not use any built-in functions or libraries to check for prime numbers, should not use any additional data structures to store intermediate results, and should be implemented in a single function without any helper functions. The solution should handle edge cases such as empty arrays or arrays with negative numbers, and should be able to handle large inputs with a maximum array size of 10^6 elements. The solution should be optimized to minimize memory usage and should have a time complexity of O(n^2) or better.
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