"""
QUESTION:
A car moves from point A to point B at speed v meters per second. The action takes place on the X-axis. At the distance d meters from A there are traffic lights. Starting from time 0, for the first g seconds the green light is on, then for the following r seconds the red light is on, then again the green light is on for the g seconds, and so on.

The car can be instantly accelerated from 0 to v and vice versa, can instantly slow down from the v to 0. Consider that it passes the traffic lights at the green light instantly. If the car approaches the traffic lights at the moment when the red light has just turned on, it doesn't have time to pass it. But if it approaches the traffic lights at the moment when the green light has just turned on, it can move. The car leaves point A at the time 0.

What is the minimum time for the car to get from point A to point B without breaking the traffic rules?

Input

The first line contains integers l, d, v, g, r (1 ≤ l, d, v, g, r ≤ 1000, d < l) — the distance between A and B (in meters), the distance from A to the traffic lights, car's speed, the duration of green light and the duration of red light.

Output

Output a single number — the minimum time that the car needs to get from point A to point B. Your output must have relative or absolute error less than 10 - 6.

Examples

Input

2 1 3 4 5


Output

0.66666667


Input

5 4 3 1 1


Output

2.33333333
"""

def calculate_minimum_time(l, d, v, g, r):
    # Calculate the time to reach the traffic lights
    z = d / v
    
    # Calculate the time to travel from the traffic lights to point B
    y = (l - d) / v
    
    # Initialize variables to track the state of the traffic light
    temp = z
    light = True
    x = 0
    
    # Determine the state of the traffic light when the car reaches it
    while True:
        if x % 2 == 0:
            if temp >= g:
                temp -= g
                light = False
            else:
                break
        elif temp >= r:
            temp -= r
            light = True
        else:
            break
        x += 1
    
    # Calculate the total time based on the state of the traffic light
    if light:
        return z + y
    else:
        return z + (r - temp) + y

# Example usage:
# result = calculate_minimum_time(2, 1, 3, 4, 5)
# print(f"{result:.8f}")