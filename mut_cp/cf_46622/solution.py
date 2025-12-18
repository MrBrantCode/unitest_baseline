"""
ORIGINAL QUESTION:
Compute the derivative of the payoff function for an American put option with respect to the underlying asset price at time 0. 

Given the payoff function g(X) = max(e^(-rt) * (K - X(t))) where X(t) is the value of the underlying at time t, K is the strike price, and r is the risk-free rate, find ∂g/∂X(0) considering the optimal stopping time τ*.
"""

def american_put_derivative(X0, K, r, tau, X_tau):
    """
    Compute the derivative of the payoff function for an American put option 
    with respect to the underlying asset price at time 0.

    Parameters:
    X0 (float): The underlying asset price at time 0.
    K (float): The strike price.
    r (float): The risk-free rate.
    tau (float): The optimal stopping time.
    X_tau (float): The value of the underlying at time tau.

    Returns:
    float: The derivative of the payoff function.
    """

    if K > X_tau:
        # Assuming dX(tau)/dX(0) = 1 for simplicity, as in the case of 
        # geometric Brownian motion without drift.
        return -math.exp(-r * tau)
    else:
        return 0