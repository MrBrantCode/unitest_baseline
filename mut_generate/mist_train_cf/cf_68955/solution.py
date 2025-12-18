"""
QUESTION:
Determine the cost multiplication of an optimal duo arrangement for a given odd prime number p, where an optimal duo arrangement is one with the least possible aggregate cost. The cost of each duo (a,b) is ab mod p, and the cost multiplication is the multiplication of the costs of its duos.

Function name: optimal_duo_arrangement_cost

Input: An odd prime number p

Restrictions: None
"""

def optimal_duo_arrangement_cost(p):
    # generate optimal duo arrangement
    duo_arrangement = [(a, p-a) for a in range(1, (p+1)//2)]
    # calculate cost multiplication
    cost_multiplication = 1
    for a, b in duo_arrangement:
        cost = a * b % p
        cost_multiplication *= cost
        cost_multiplication %= p  # to prevent overflow
    return cost_multiplication