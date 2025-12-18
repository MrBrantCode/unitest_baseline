"""
QUESTION:
Calculate the distance two cars will be apart after driving in opposite directions and determine when they will reach a specific distance. 

Function: `calculate_distance` 
Input: 
- Initial speeds `S1` and `S2` 
- Initial time `T` 
- Modified speeds `S1_prime` and `S2_prime` 
- Distance `D` (for the second part of the problem) 

Output: 
- Total distance the cars will be apart 
- Time `T` when the cars will be a specific distance `D` apart 

Restrictions: 
- Cars start from the same point and drive in opposite directions 
- Cars drive for `T` hours with initial speeds and then change their speeds 
- If the desired distance `D` is larger than the total distance the cars can cover, return an impossible result.
"""

def calculate_distance(S1, S2, T, S1_prime, S2_prime, D):
    """
    Calculate the total distance two cars will be apart and the time they will reach a specific distance.
    
    Args:
        S1 (float): Initial speed of car 1.
        S2 (float): Initial speed of car 2.
        T (float): Initial time in hours.
        S1_prime (float): Modified speed of car 1.
        S2_prime (float): Modified speed of car 2.
        D (float): Specific distance apart.
    
    Returns:
        tuple: Total distance the cars will be apart, time when they will be a specific distance apart.
    """

    # Calculate the total distance the cars will be apart
    total_distance = (S1 + S2) * T + (S1_prime + S2_prime) * T

    # Check if the desired distance is larger than the total distance the cars can cover
    if D > total_distance:
        return total_distance, "Impossible"

    # Calculate the time when the cars will be a specific distance apart
    if D <= (S1 + S2) * T:
        time_apart = D / (S1 + S2)
    else:
        time_apart = T + (D - (S1 + S2) * T) / (S1_prime + S2_prime)

    return total_distance, time_apart