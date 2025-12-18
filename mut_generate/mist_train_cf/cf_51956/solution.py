"""
QUESTION:
Create a function `compute_cubes(n)` that dynamically generates the first `n` prime numbers and computes their cubes, displaying the results in the console-based output. The prime numbers should be generated using a prime-checking algorithm within the program, and the function should handle possible errors or exceptions. The function should only use a single while loop to traverse through the prime numbers.
"""

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True

    if n % 2 == 0 or n % 3 == 0:
        return False

    i = 5
    while(i * i <= n):
        if (n % i == 0 or n % (i + 2) == 0):
            return False
        i += 6

    return True

def compute_cubes(n):
    i = 2
    primes = []
    
    try:
        while len(primes) < n:
            if is_prime(i):
                primes.append(i)
            i += 1

        for prime in primes:
            print(f"Cubic of {prime} is {prime**3}")

    except Exception as e:
        print(f"An error occurred: {str(e)}")