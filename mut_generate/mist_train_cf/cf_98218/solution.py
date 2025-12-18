"""
QUESTION:
Write a function named `prime_numbers` that takes a list of unique integers as input, sorted in descending order. The function should return a tuple containing the sum of all prime numbers in the list, the largest prime number, the smallest prime number, and the count of prime numbers. Exclude negative numbers and zero from the calculation. The function should be able to handle lists of any size and should not use any external libraries or modules.
"""

def entrance(arr):
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
            if largest_prime is None or num > largest_prime:
                largest_prime = num
            if smallest_prime is None or num < smallest_prime:
                smallest_prime = num
    
    # Return results
    return prime_sum, largest_prime, smallest_prime, prime_count