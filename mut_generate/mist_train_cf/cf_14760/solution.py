"""
QUESTION:
Create a function called `count_ways` that calculates the number of different ways to climb `n` stairs, with the constraint that you can only climb 1, 2, or 3 stairs at a time. The function should take an integer `n` as input and return the total number of ways to climb `n` stairs.
"""

def count_ways(n):
    # Initialize a list to store the number of ways to climb each number of stairs
    ways = [0] * (n + 1)
    
    # There is only one way to climb 0 stairs (by not climbing)
    ways[0] = 1
    # There is one way to climb 1 stair (by taking one step)
    if n >= 1: ways[1] = 1
    # There are two ways to climb 2 stairs (by taking two steps or two single steps)
    if n >= 2: ways[2] = 2
    
    # Iterate through all the possible number of stairs
    for i in range(3, n + 1):
        # Calculate the number of ways to climb i stairs by considering the three possible previous steps
        ways[i] = ways[i - 1] + ways[i - 2] + ways[i - 3]
    
    return ways[n]