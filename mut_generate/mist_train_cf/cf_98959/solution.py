"""
QUESTION:
Create a function `make_friends` that simulates Ernest's attempts to make friends with victims in a neighborhood. The function should take a list of tuples representing the victims, where each tuple contains a string name and an integer age. The function should return the number of days it takes for Ernest to make friends with all eligible victims. A victim is eligible if their name starts with the letter "E" and their age is a prime number. If Ernest cannot make friends with all eligible victims within 30 days, the function should return -1.
"""

import math

def make_friends(victims):
    """
    Simulates Ernest's attempts to make friends with victims in a neighborhood.
    
    Args:
    victims (list): A list of tuples representing the victims, where each tuple contains a string name and an integer age.
    
    Returns:
    int: The number of days it takes for Ernest to make friends with all eligible victims. Returns -1 if Ernest cannot make friends with all eligible victims within 30 days.
    """
    
    # Set of victims Ernest has approached
    approached = set()
    
    # Number of days it takes to make friends with all eligible victims
    days = 0
    
    # Loop until Ernest has approached all eligible victims or 30 days have passed
    while len(approached) < len(victims) and days < 30:
        # Find the next eligible victim to approach
        victim = next((v for v in victims if v[0][0] == "E" and v[1] > 1 and all(v[1] % i != 0 for i in range(2, int(math.sqrt(v[1]))+1)) and v not in approached), None)
        
        # If no eligible victim is found, return -1
        if victim is None:
            return -1
        
        # Ernest approaches the victim
        approached.add(victim)
        days += 1
    
    # Return the number of days it took to make friends with all eligible victims
    return days if len(approached) == len(victims) else -1