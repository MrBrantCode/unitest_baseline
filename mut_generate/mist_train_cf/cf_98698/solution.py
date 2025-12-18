"""
QUESTION:
Implement a function called `gradient_descent` that performs Elastic Net Regression on a given dataset. The function should take in the following parameters: `X` (feature matrix), `y` (target vector), `theta` (initial coefficients), `alpha` (regularization parameter), `rho` (Elastic Net mixing parameter), and `num_iters` (number of iterations). The function should return the updated coefficients and the cost history. The implementation should not use any external libraries or packages.
"""

def elastic_net_regression(X, y, theta, alpha, rho, num_iters):
    m = len(y)
    J_history = []
    for i in range(num_iters):
        h = X.dot(theta)
        theta -= alpha * (1 / m * X.T.dot(h - y) + alpha / m * ((1 - rho) * theta + rho * np.sign(theta)))
        J_history.append(cost_function(theta, X, y, alpha, rho))
    return theta, J_history


def cost_function(theta, X, y, alpha, rho):
    m = len(y)
    h = X.dot(theta)
    J = 1 / (2 * m) * np.sum((h - y) ** 2) + alpha / (2 * m) * ((1 - rho) * np.sum(theta ** 2) + rho * np.sum(np.abs(theta)))
    return J