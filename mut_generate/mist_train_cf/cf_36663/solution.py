"""
QUESTION:
Create a function `simulate_exponential_growth` that simulates a simple exponential growth process using the Euler method. The function should take four parameters: `initial_quantity`, `growth_rate`, `time_step`, and `num_steps`, and return a list of quantities at each time step. The Euler method should be used to approximate the solution of the differential equation dy/dt = ky, where y is the quantity, t is time, and k is the growth rate. The function should handle the case where the growth rate is negative, representing exponential decay.
"""

def simulate_exponential_growth(initial_quantity, growth_rate, time_step, num_steps):
    quantities = [initial_quantity]  
    current_quantity = initial_quantity  

    for _ in range(num_steps):
        next_quantity = current_quantity + growth_rate * current_quantity * time_step
        quantities.append(next_quantity)  
        current_quantity = next_quantity  

    return quantities