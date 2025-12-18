"""
QUESTION:
Implement a function `flow_rule_study_height_angle` that calculates the height and angle of a projectile at a specified time. The function takes four required parameters: `initial_velocity` (in m/s), `launch_angle` (in degrees), `time` (in seconds), and an arbitrary number of additional arguments. The function can optionally take two flags: `-tmax` to specify a maximum time (in seconds), and `-oldValues` to use old values in the calculation. The function returns the height (in meters) and angle (in degrees) of the projectile at the specified time.
"""

import math

def flow_rule_study_height_angle(initial_velocity, launch_angle, time, *args):
    tmax_flag_index = args.index('-tmax') if '-tmax' in args else -1
    old_values_flag_index = args.index('-oldValues') if '-oldValues' in args else -1

    if tmax_flag_index != -1:
        tmax = float(args[tmax_flag_index + 1])
    else:
        tmax = None

    if old_values_flag_index != -1:
        use_old_values = True
    else:
        use_old_values = False

    g = 9.81  
    theta = math.radians(launch_angle)
    vx = initial_velocity * math.cos(theta)
    vy = initial_velocity * math.sin(theta)

    if tmax is not None and time > tmax:
        time = tmax

    if use_old_values:
        height = vy * time - 0.5 * g * time ** 2
        angle = math.degrees(math.atan(vy / vx))
    else:
        height = vy * time - 0.5 * g * time ** 2
        angle = launch_angle

    return height, angle