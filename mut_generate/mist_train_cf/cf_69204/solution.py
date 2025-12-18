"""
QUESTION:
Compute the initial speeds of two rockets, Rocket A and Rocket B, which are traveling in opposite directions. The speed of Rocket A is three times that of Rocket B. On the nth minute, Rocket A increases its speed by n km/h and then resumes its original speed, while Rocket B increases its speed by n/2 km/h and then resumes its original speed. Given the acceleration boost timings 'n_A' and 'n_B' in minutes for both rockets and the distance 'distance' apart in km at the end of two hours, compute and return the initial constant speeds of the two rockets in km/h. Assume the acceleration boost timings and distance apart are the only inputs.
"""

def rocket_speeds(n_A, n_B, distance):
    # Convert minutes to hours
    n_A /= 60
    n_B /= 60
    
    # The distance equation is based on the formula: d = vt + 0.5at^2
    # For Rocket A: distance_A = speed_A * 2 + 0.5 * n_A * 2
    # For Rocket B: distance_B = speed_B * 2 + 0.5 * n_B * 2
    # The total distance is: distance = distance_A + distance_B
    # which can be rewritten as: distance = (speed_A + speed_B) * 2 + (0.5 * n_A + 0.5 * n_B) * 2
    # After rearranging the equation, we can solve for speed_A and speed_B
    speed_A = (distance - (n_A + n_B)) / 4
    speed_B = speed_A / 3  # Rocket A's speed is 3 times Rocket B's speed

    return speed_A, speed_B