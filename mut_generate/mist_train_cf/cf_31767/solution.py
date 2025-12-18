"""
QUESTION:
Create a function called `sir_model` that implements the SIR model equations to simulate the spread of a disease. The function should take as input the number of susceptible individuals `S`, the number of infected individuals `I`, the number of recovered individuals `R`, the transmission rate `beta`, and the recovery rate `gamma`. The function should return the derivatives `dSdt`, `dIdt`, and `dRdt` that represent the rate of change of the susceptible, infected, and recovered populations with respect to time.
"""

def sir_model(S, I, R, beta, gamma):
    """
    SIR model equations to simulate the spread of a disease.

    Parameters:
    S (int): Number of susceptible individuals
    I (int): Number of infected individuals
    R (int): Number of recovered individuals
    beta (float): Transmission rate
    gamma (float): Recovery rate

    Returns:
    tuple: Derivatives dSdt, dIdt, dRdt representing the rate of change of the susceptible, infected, and recovered populations with respect to time.
    """
    N = S + I + R  # Total population size
    dSdt = -beta * S * I / N
    dIdt = beta * S * I / N - gamma * I
    dRdt = gamma * I
    return dSdt, dIdt, dRdt