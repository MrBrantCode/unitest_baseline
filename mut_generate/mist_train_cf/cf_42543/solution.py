"""
QUESTION:
Implement the `compute_log_derivative` method in the `dRQP_dellp` class to compute the log-derivative of the function with respect to the parameter `ell_p`. The method should take a single argument `r` and return the value of the log-derivative at the given input `r`. The function is defined as:

\[ f(r) = \frac{\text{weight}}{\ell_p^2} \cdot \exp\left(-2 \cdot \sin^2\left(\pi \cdot \left|\frac{r}{P}\right|\right)/\ell_p^2\right) \cdot \left(1 + \frac{r^2}{2 \cdot \alpha \cdot \ell_e^2}\right)^{-\alpha} \cdot P \]

Where:
- `weight`, `alpha`, `ell_e`, `P`, and `ell_p` are parameters of the function.
- `r` is a variable representing the input to the function.
- The log-derivative is defined as the derivative of the logarithm of a function with respect to a parameter.
"""

def compute_log_derivative(r, weight, alpha, ell_e, P, ell_p):
    """
    Compute the log-derivative of the function with respect to ell_p at input r
    """
    sine_term = np.sin(np.pi * np.abs(r) / P)
    exp_term = np.exp(-2 * sine_term**2 / ell_p**2)
    power_term = (1 + r**2 / (2 * alpha * ell_e**2))**(-alpha)
    log_derivative = (weight / ell_p**2) * exp_term * power_term * P * (-2 * sine_term**2 / ell_p**3)
    return log_derivative