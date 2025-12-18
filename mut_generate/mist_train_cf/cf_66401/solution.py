"""
QUESTION:
Write a function called `deriv` that models the Lotka-Volterra predator-prey interaction using a system of differential equations. The function should take a list `y` containing the rabbit and fox populations, and a time `t`, and return the derivatives of the rabbit and fox populations with respect to time. The rabbit population grows at a rate `alpha` and is reduced by interactions with foxes at a rate `beta`, while the fox population grows at a rate `delta` proportional to interactions with rabbits and decreases at a rate `gamma`. The function should not include any numerical integration or plotting code.
"""

def deriv(y, t, alpha, beta, delta, gamma):
    rabbits, foxes = y
    drdt = alpha * rabbits - beta * rabbits * foxes
    dfdt = delta * rabbits * foxes - gamma * foxes
    return drdt, dfdt