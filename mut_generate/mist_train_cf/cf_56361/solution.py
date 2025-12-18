"""
QUESTION:
Write a function `total_ways(members, females, males, sub_roles)` that calculates the total number of ways to assign roles for a theatrical performance. The function should take four parameters: the total number of members, the number of females, the number of males, and the number of distinct sub-roles. The function should return the total number of ways to assign one female lead, one male lead, and the sub-roles, considering that the sub-roles can be played by actors of any gender and the order of assignment matters.
"""

import math

def total_ways(members, females, males, sub_roles):
    # Calculate the number of ways to select the leads
    leads_ways = math.comb(females, 1) * math.comb(males, 1)

    # After selecting the leads, calculate the remaining members
    remaining_members = members - 2  # 2 leads have been selected

    # Calculate the number of ways to assign the sub_roles
    sub_roles_ways = math.perm(remaining_members, sub_roles)

    # The total ways is the product of the ways to select the leads and the ways to assign the sub_roles
    total_ways = leads_ways * sub_roles_ways

    return total_ways