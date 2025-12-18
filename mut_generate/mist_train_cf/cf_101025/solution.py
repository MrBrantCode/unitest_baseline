"""
QUESTION:
Implement a function `gradient_descent` that uses Elastic Net Regression, a regularized linear regression model that combines Lasso and Ridge regression. The function should take in the following parameters: feature matrix `X`, target variable `y`, initial coefficients `theta`, regularization parameter `alpha`, Elastic Net mixing parameter `rho`, and the number of iterations `num_iters`. It should return the updated coefficients `theta` and the history of cost values `J_history`. The function should not use any external libraries or packages.
"""

def gradient_descent(X, y, theta, alpha, rho, num_iters):
    m = len(y)
    J_history = [0.0] * num_iters
    for i in range(num_iters):
        h = [sum(x * t for x, t in zip(row, theta)) for row in X]
        for j in range(len(theta)):
            derivative = sum((h[k] - y[k]) * X[k][j] for k in range(m)) / m + alpha / m * ((1 - rho) * theta[j] + rho * (1 if theta[j] > 0 else (-1 if theta[j] < 0 else 0)))
            theta[j] -= alpha * derivative
        J_history[i] = 1 / (2 * m) * sum((h[k] - y[k]) ** 2 for k in range(m)) + alpha / (2 * m) * ((1 - rho) * sum(t ** 2 for t in theta) + rho * sum(abs(t) for t in theta))
    return theta, J_history