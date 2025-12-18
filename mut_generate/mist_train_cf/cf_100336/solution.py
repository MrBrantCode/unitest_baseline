"""
QUESTION:
Implement the AdaGrad algorithm to optimize the parameters of a model given a set of training data. The function should take as input the feature matrix X, the target vector y, the initial parameters theta, the learning rate alpha, the number of iterations, and the epsilon value (default is 1e-8). The function should return the optimized parameters theta and the history of the cost function at each iteration.
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