"""
QUESTION:
Write a function `prime_numbers` that takes a list of integers as input and returns the sum of all the prime numbers, the largest prime number, the smallest prime number, and the total count of prime numbers in the list. The input list should be in descending order before processing, and the function should exclude negative numbers and zero from the calculation. The function should not use any external libraries or modules and should be able to handle lists of any size with unique integers.
"""

def entance(arr):
    # Sort the array in descending order
    arr.sort(reverse=True)
    
    # Initialize variables
    prime_sum = 0
    prime_count = 0
    largest_prime = None
    smallest_prime = None
    
    # Check each number in the array
    for num in arr:
        # Exclude negative numbers and zero
        if num <= 1:
            continue
        
        # Check if the number is prime
        is_prime = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        
        # If the number is prime, update variables
        if is_prime:
            prime_sum += num
            prime_count += 1
            if largest_prime is None:
                largest_prime = num
            if smallest_prime is None:
                smallest_prime = num
            if num > largest_prime:
                largest_prime = num
            if num < smallest_prime:
                smallest_prime = num
    
    # Return results
    return prime_sum, largest_prime, smallest_prime, prime_count