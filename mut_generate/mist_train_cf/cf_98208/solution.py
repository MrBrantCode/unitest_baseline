"""
QUESTION:
Write a function `find_winner` that takes no arguments. The function simulates a ball being passed around a circle of 64 people, with each person having a unique number from 1 to 64. The ball is passed to the person whose position in the circle is the closest prime number greater than the previous position. The function returns the number on the shirt of the last person to receive the ball.
"""

def is_prime(n):
    """Check if a number is prime."""
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def find_winner():
    n = 64
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