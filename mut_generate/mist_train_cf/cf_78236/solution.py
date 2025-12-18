"""
QUESTION:
Write a function `sophisticatedDivisorContest(n)` that determines whether Alice can win a turn-based game where she and Bob take turns subtracting divisors from a number `n`. If `n` is prime, players must subtract prime divisors; otherwise, they can subtract any divisor. A player loses if they cannot make a move. Assume both players use optimal strategies. The function should return `True` if Alice wins and `False` otherwise. The input `n` is an integer with `2 <= n <= 1000`.
"""

def sophisticatedDivisorContest(n):
    def isPrime(n):
        if n <= 1:
            return False
        elif n <= 3:
            return True
        elif n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True

    return not isPrime(n) or n == 2