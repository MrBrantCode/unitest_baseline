"""
QUESTION:
Create a function called `mersenne_prime` that takes an integer `n` as input and returns the steps to determine whether `n` is a Mersenne prime number. A Mersenne prime is a prime number that can be written in the form 2^n - 1 for some integer `n`. The function should test if `n` is prime and if 2^n - 1 is also prime, then return the steps taken to make this determination. The steps should be returned as a string with each step on a new line.
"""

def is_prime(number):
    if number <= 1:
        return [number, "is not prime"]
    elif number == 2:
        return [number, "is prime"]
    elif number % 2 == 0:
        return [number, "is not prime"]
    elif number > 2:
        i = 3
        while i * i <= number:
            if number % i:
                i += 2
            else:
                return [number, "is not prime"]
        return [number, "is prime"]

def mersenne_prime(n):
    steps = []
    if is_prime(n)[1] == "is prime":
        steps.append(f"Step 1: {n} is a prime number.")
        mersenne_number = 2**n - 1
        if is_prime(mersenne_number)[1] == "is prime":
            steps.append(f"Step 2: {mersenne_number} is a prime number.")
            steps.append(f"Step 3: Consequently, {n} is a Mersenne prime.")
        else:
            steps.append(f"Step 2: However, {mersenne_number} is not a prime number.")
            steps.append(f"Step 3: Consequently, {n} is not a Mersenne prime.")
    else:
        steps.append(f"Step 1: {n} is not a prime number.")
        steps.append(f"Step 2: Consequently, {n} is not a Mersenne prime.")
  
    return '\n'.join(steps)