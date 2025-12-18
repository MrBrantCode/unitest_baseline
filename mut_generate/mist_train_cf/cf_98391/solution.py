"""
QUESTION:
Create a function named `evaluate_expression` that takes a string representing a mathematical expression as input, evaluates the expression, and returns the result along with a list of all prime numbers used in the expression. Use a helper function named `is_prime` to check for primality.
"""

def evaluate_expression(expr):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5)+1):
            if n % i == 0:
                return False
        return True

    primes = []
    result = eval(expr)
    for num in re.findall(r'\d+', expr):
        if is_prime(int(num)):
            primes.append(int(num))
    return result, primes