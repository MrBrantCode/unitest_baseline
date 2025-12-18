"""
QUESTION:
Implement the `finite_difference_method` function, which simulates a one-dimensional heat conduction problem using the finite difference method. The function should take the initial temperature distribution `initial_temp`, the thermal conductivity constant `thermal_conductivity`, and the number of time steps `num_time_steps` as input, and return the temperature distribution at the final time step.

The temperature at each interior point is updated based on the temperatures of neighboring points and the material's thermal conductivity, using the formula: `u[1:-1] = u[1:-1] - 2 * c * (u[1:-1] - u[:-2])`. The boundary points are assumed to be fixed and do not change during the simulation.
"""

from typing import List

def finite_difference_method(initial_temp: List[float], thermal_conductivity: float, num_time_steps: int) -> List[float]:
    current_temp = initial_temp[:]
    num_points = len(initial_temp)
    
    for _ in range(num_time_steps):
        new_temp = current_temp[:]
        for i in range(1, num_points - 1):
            new_temp[i] = current_temp[i] - 2 * thermal_conductivity * (current_temp[i] - current_temp[i-1])
        current_temp = new_temp
    
    return current_temp