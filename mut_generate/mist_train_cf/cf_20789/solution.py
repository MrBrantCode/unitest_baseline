"""
QUESTION:
Create a function named `PrimeKeyGenerator` that takes an initial key value and returns an object that, on every call of its `generate_next_key` method, increments the key by the next prime number.
"""

def PrimeKeyGenerator(initial_key):
    class KeyGenerator:
        def __init__(self):
            self.current_key = initial_key
            self.primes = [2]

        def is_prime(self, num):
            for prime in self.primes:
                if num % prime == 0:
                    return False
            return True

        def generate_next_key(self):
            while True:
                self.current_key += 1
                if self.is_prime(self.current_key):
                    self.primes.append(self.current_key)
                    return self.current_key

    return KeyGenerator()

# Usage example:
generator = PrimeKeyGenerator(10)
for _ in range(5):
    next_key = generator.generate_next_key()
    print(next_key)