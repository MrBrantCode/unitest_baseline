"""
QUESTION:
Find the function of the eastern car's speed f(t) and the speed p of the western car given the distance d(t) between them. The eastern car's speed is given by f(t) = t² + 2t + 1.5 and the western car's speed p is constant. The distance d(t) is the sum of the distances traveled by each car.
"""

def entrance(f, p, d):
    """
    Calculates the speed function of the eastern car and the speed of the western car.
    
    Args:
        f (function): The speed function of the eastern car.
        p (float): The speed of the western car.
        d (function): The distance between the two cars.
    
    Returns:
        tuple: A tuple containing the speed function of the eastern car and the speed of the western car.
    """
    # Calculate the distance traveled by the eastern car
    def eastern_distance(t):
        return (1/3)*t**3 + t**2 + 1.5*t
    
    # Calculate the distance traveled by the western car
    def western_distance(t):
        return d(t) - eastern_distance(t)
    
    # Calculate the speed of the western car
    def western_speed(t):
        return western_distance(t) / t
    
    return f, western_speed