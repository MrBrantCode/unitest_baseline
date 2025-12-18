"""
QUESTION:
Implement the `adagrad` function, which takes in the following parameters: `X`, `y`, `theta`, `alpha`, `num_iters`, and `eps`. The function should return the optimal parameters `theta` and the history of cost values `J_history`. The function should use the AdaGrad algorithm with a varying learning rate to update the parameters.

Restrictions: The function should use the AdaGrad algorithm with a varying learning rate, where the learning rate is adjusted based on the historical sum of squares of the gradients. The function should also handle the case where the gradient becomes zero to avoid division by zero errors.

Note: The `eps` parameter is a small positive value used to avoid division by zero errors.
"""

def adagrad(X, y, theta, alpha, num_iters, eps=1e-8):
    J_history = np.zeros(num_iters)
    G = np.zeros_like(theta)
    for i in range(num_iters):
        h = np.dot(X, theta)
        grad = 1 / y.size * np.dot(X.T, h - y)
        G += np.square(grad)
        theta -= alpha / (np.sqrt(G) + eps) * grad
        J_history[i] = np.sum(np.square(np.dot(X, theta) - y)) / (2 * y.size)
    return theta, J_history