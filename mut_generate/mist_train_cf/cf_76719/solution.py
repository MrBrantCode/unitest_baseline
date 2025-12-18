"""
QUESTION:
Develop a function `calculate_stats(n)` that calculates the aggregate, mean, median, and standard deviation of the initial n prime numbers. The function should handle fringe scenarios where n is less than 1 or a non-integer value by returning an error message. Implement a value check at the start of the function to detect and handle these edge cases correctly.
"""

def calculate_stats(n):
    if isinstance(n, int) and n > 0:
        primes = []
        num = 2
        while len(primes) != n:
            for i in range(2, num):
                if num % i == 0:
                    break
            else:
                primes.append(num)
            num += 1
        
        total = sum(primes)
        mean = total / n
        median = primes[n // 2] if n % 2 == 1 else (primes[n // 2 - 1] + primes[n // 2]) / 2
        deviation = (sum((i - mean) ** 2 for i in primes) / n) ** 0.5
        
        return total, mean, median, deviation
    else:
        return "Error: Invalid input. Please enter a positive integer."