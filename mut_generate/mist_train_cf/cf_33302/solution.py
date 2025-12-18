"""
QUESTION:
Implement a Python function `joint_pdf(marg_value_x, marg_value_y, x_mu, x_sigma, y_mu, y_sigma, correlation_coefficient)` that takes in the marginal values of X and Y as input, along with their respective means, standard deviations, and correlation coefficient, and returns the joint probability density function (PDF) as a 2D array. 

The function should calculate the joint PDF using the formula: 
\[ f(x, y) = \frac{1}{2\pi\sigma_x\sigma_y\sqrt{1-\rho^2}} \exp\left(-\frac{1}{2(1-\rho^2)}\left[\frac{(x-\mu_x)^2}{\sigma_x^2} - 2\rho\frac{(x-\mu_x)(y-\mu_y)}{\sigma_x\sigma_y} + \frac{(y-\mu_y)^2}{\sigma_y^2}\right]\right) \]

Where:
- `marg_value_x` and `marg_value_y` are lists containing the marginal values of X and Y respectively.
- `x_mu` and `y_mu` are the means of X and Y.
- `x_sigma` and `y_sigma` are the standard deviations of X and Y.
- `correlation_coefficient` is the correlation coefficient between X and Y.
"""

import numpy as np

def joint_pdf(marg_value_x, marg_value_y, x_mu, x_sigma, y_mu, y_sigma, correlation_coefficient):
    joint_pdf_values = []
    for x in marg_value_x:
        row = []
        for y in marg_value_y:
            exponent = -1 / (2 * (1 - correlation_coefficient**2)) * (
                ((x - x_mu)**2) / (x_sigma**2) - 2 * correlation_coefficient * ((x - x_mu) * (y - y_mu)) / (x_sigma * y_sigma) + ((y - y_mu)**2) / (y_sigma**2)
            )
            pdf_value = 1 / (2 * np.pi * x_sigma * y_sigma * np.sqrt(1 - correlation_coefficient**2)) * np.exp(exponent)
            row.append(pdf_value)
        joint_pdf_values.append(row)
    return joint_pdf_values