"""
QUESTION:
Implement the `build_grad_batched(network, batch_size)` function, which computes the average gradient for a given neural network by splitting the inputs into batches of a specified size and then averaging the gradients. The function takes in two parameters: `network`, a neural network for which the average gradient needs to be computed, and `batch_size`, an integer representing the size of each batch for splitting the inputs. The `build_grad(network)` function is assumed to be already implemented and returns the gradient of the network. The `build_grad_batched` function should return a new function that takes in inputs `(X, y, w)` and returns the average gradient.
"""

def build_grad_batched(network, batch_size):
    """Compute the average gradient by splitting the inputs in batches of size
    'batch_size' and averaging."""
    grad = build_grad(network)
    def inner(X, y, w):
        N = len(X)
        g = 0
        for i in range(0, N, batch_size):
            batch_X = X[i:i+batch_size]
            batch_y = y[i:i+batch_size]
            batch_grad = grad((batch_X, batch_y, w))
            g += batch_grad
        average_grad = g / (N / batch_size)  # Compute the average gradient
        return average_grad
    return inner