"""
QUESTION:
Write a function named `update_weights` that takes in parameters `weights`, `x`, `y`, `learning_rate`, `decay_factor`, `decay_interval`, `rho`, `epsilon`, `lambda_val`, and `num_epochs`. The function should implement the RMSprop optimization algorithm with L1 regularization to update the weights for a specified number of epochs. The learning rate should decay at the specified interval using the given decay factor.
"""

def update_weights(weights, x, y, learning_rate, decay_factor, decay_interval, rho, epsilon, lambda_val, num_epochs):
    v = 0
    for epoch in range(num_epochs):
        if epoch % decay_interval == 0 and epoch != 0:
            learning_rate *= decay_factor
        gradients = (2 * x * (x * weights - y) + lambda_val)
        v = rho * v + (1 - rho) * gradients ** 2
        weights -= learning_rate * gradients / (epsilon + v ** 0.5)
    return weights