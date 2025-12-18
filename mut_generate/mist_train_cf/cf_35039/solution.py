"""
QUESTION:
Write a Python function named `lotka_volterra_simulation` that simulates a predator-prey model using the Lotka-Volterra equations for a specified number of generations. The function should take as input the initial prey population, initial predator population, prey growth rate, predation rate, predator death rate, predator growth rate, and the number of generations to simulate. It should then return the prey and predator populations at each generation.

The Lotka-Volterra equations are given by:
\[ \frac{dP}{dt} = aP - bPC \]
\[ \frac{dC}{dt} = -cC + dPC \]

Where:
- `P` represents the prey population
- `C` represents the predator population
- `a` is the prey growth rate
- `b` is the predation rate
- `c` is the predator death rate
- `d` is the predator growth rate

Note that the function should not take any user input. Instead, it should be a reusable function that can be called with different input values.
"""

def lotka_volterra_simulation(prey, predator, a, b, c, d, generations):
    """
    Simulate a predator-prey model using the Lotka-Volterra equations for a specified number of generations.

    Args:
        prey (int): Initial prey population
        predator (int): Initial predator population
        a (float): Prey growth rate
        b (float): Predation rate
        c (float): Predator death rate
        d (float): Predator growth rate
        generations (int): Number of generations to simulate

    Returns:
        tuple: A tuple of lists, where the first list contains the prey population at each generation and the second list contains the predator population at each generation
    """

    # Initialize lists to store the prey and predator populations at each generation
    prey_populations = [prey]
    predator_populations = [predator]

    # Simulate predator-prey model for the specified number of generations
    for _ in range(generations):
        # Calculate the change in prey and predator populations using the Lotka-Volterra equations
        dP_dt = a * prey - b * prey * predator
        dC_dt = -c * predator + d * prey * predator

        # Update the prey and predator populations
        prey += dP_dt
        predator += dC_dt

        # Store the updated prey and predator populations
        prey_populations.append(prey)
        predator_populations.append(predator)

    # Return the prey and predator populations at each generation
    return prey_populations, predator_populations