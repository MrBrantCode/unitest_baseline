"""
QUESTION:
In a group of `n` people, each with a unique number from 1 to `n`, the ball is passed in a circle following this pattern: the ball is passed to the person whose position is the closest prime number greater than the previous position. Write a function `find_winner(n)` that returns the number on the shirt of the last person to receive the ball. The function should work for any positive integer `n`.
"""

def find_winner(n):
    def is_prime(num):
        """Check if a number is prime."""
        if num < 2:
            return False
        for i in range(2, int(num**0.5)+1):
            if num % i == 0:
                return False
        return True

    people = list(range(1, n+1))
    pos = 0  # starting position of the ball
    while len(people) > 1:
        # find the next prime number greater than the current position
        prime_pos = pos + 1
        while not is_prime(prime_pos):
            prime_pos += 1
        prime_pos %= len(people)  # wrap around if necessary
        # pass the ball to the next person
        pos = prime_pos
        people.pop(pos)
    return people[0]