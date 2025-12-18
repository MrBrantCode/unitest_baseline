"""
QUESTION:
Write a function `closest_prime_integer` that takes a value as input and returns the closest prime integer to the input value. If the input value is a float, it should be rounded to the nearest integer. The function should return the lower prime integer if the input value is equidistant from two prime integers. If the input is not a valid number, the function should return "Error: Invalid input."
"""

def closest_prime_integer(value):
    def is_prime(n):
        if n == 2 or n == 3: return True
        if n < 2 or n%2 == 0: return False
        if n < 9: return True
        if n%3 == 0: return False
        r = int(n**0.5)
        f = 5
        while f <= r:
            if n%f == 0: return False
            if n%(f+2) == 0: return False
            f +=6
        return True 

    def next_prime(n):
        if n <= 1:
            return 2
        prime = n
        found = False
        while not found:
            prime += 1
            if is_prime(prime):
                found = True
        return prime

    def prev_prime(n):
        if n <= 1:
            return 2
        prime = n
        found = False
        while not found:
            prime -= 1
            if is_prime(prime):
                found = True
        return prime

    try:
        n = round(float(value))
        if is_prime(n):
            return n
        else:
            lower = prev_prime(n)
            upper = next_prime(n)
            if n - lower < upper - n:
                return lower
            else:
                return upper
    except ValueError:
        return "Error: Invalid input."