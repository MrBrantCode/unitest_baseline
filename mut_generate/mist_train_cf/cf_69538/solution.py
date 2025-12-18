"""
QUESTION:
Write a function `solve(num_heads, num_legs)` that determines the quantities of snakes, crocodiles, and tortoises in a cage. The function should take the total number of heads (`num_heads`) and the total number of legs (`num_legs`) as input, where each snake has one head and no legs, each crocodile has one head and four legs, and each tortoise has one head and four legs. The function should return the number of snakes, crocodiles, and tortoises as output, or 'No Solution' if no valid quantities exist.
"""

def solve(num_heads, num_legs):
    for num_snakes in range(num_heads + 1):
        num_croc_and_tort = num_heads - num_snakes
        total_legs = 4 * num_croc_and_tort
        if total_legs == num_legs:
            return num_snakes, num_croc_and_tort, num_croc_and_tort
    return 'No Solution'