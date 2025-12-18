"""
QUESTION:
Write a function called `convert_to_reverse_prime_number` that takes an array of positive integers as input, converts the prime numbers in the array to strings, reverses their order, and concatenates them into a single string. The function should return this string, excluding non-prime numbers from the array.
"""

def convert_to_reverse_prime_number(arr):
    result = ""
    
    # Iterate through the input array in reverse order
    for num in reversed(arr):
        # Check if the number is prime
        is_prime = True
        if num > 1:
            for i in range(2, int(num/2) + 1):
                if (num % i) == 0:
                    is_prime = False
                    break
        
        # If the number is prime, convert it to a string and append it to the result string
        if is_prime:
            result += str(num)
    
    return result