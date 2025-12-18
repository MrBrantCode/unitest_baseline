"""
QUESTION:
Construct a recursive function `sequence` that generates an alternating sequence of prime and composite numbers within the range 3 to 100. The sequence should start with a prime number, followed by a composite number, and maintain this pattern, skipping numbers that do not match the required type. A number is prime if it has only two unique divisors (1 and itself) and composite if it has more than two unique divisors.
"""

def sequence(n=3, toggle=True):
    if n > 100:
        return
    # Generate prime numbers
    if toggle and is_prime(n):
        result.append(n)
        sequence(n+1, not toggle)
    # Generate composite numbers
    elif not toggle and not is_prime(n):
        result.append(n)
        sequence(n+1, not toggle)
    else:
        sequence(n+1, toggle)

def is_prime(n):
    if n == 1:
        return False
    if n == 2:
        return True
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True