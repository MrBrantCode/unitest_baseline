"""
QUESTION:
Write a function named `solve_problem` that takes a list of integers as input and returns a dictionary containing the median of the five largest prime numbers, the median of the five smallest prime numbers, and the second largest prime number in the original order. If the list contains fewer than five prime numbers, the function should return `None`. The function should treat duplicate prime numbers as separate entries.
"""

def is_prime(n):
    """Check if number is prime"""
    if n == 1 or n ==0:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def solve_problem(lst):
    """Solve the problem"""
    primes = [n for n in lst if is_prime(n)]
    
    # if there are less than 5 prime numbers
    if len(primes) < 5:
        return None
    
    primes_sorted = sorted(primes)
    least_five = primes_sorted[:5]
    most_five = primes_sorted[-5:]
    
    median_least = least_five[len(least_five) // 2]
    median_most = most_five[len(most_five) // 2]
    
    # find the second largest prime number in the original order
    primes_no_duplicates = list(dict.fromkeys(primes))  # remove duplicates while maintaining original order
    second_largest_in_order = sorted(primes_no_duplicates)[-2]
    
    return {"median_least": median_least, "median_most": median_most, "second_largest_in_order": second_largest_in_order}