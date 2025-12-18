"""
QUESTION:
Implement a Python function `calculate_gaussian_likelihood` that manually calculates the Gaussian likelihood for each data point in a batch. The function should take three arguments: a 2D array `x` of shape `(batch_size, dim)` representing the input data points, a 2D array `mu` of shape `(batch_size, dim)` representing the mean of the Gaussian distribution, and a 1D array `log_std` of shape `(dim)` representing the log standard deviation of the Gaussian distribution. The function should return a list of Gaussian likelihoods for each data point in the batch without using any external libraries.
"""

def calculate_gaussian_likelihood(x, mu, log_std):
    batch_size, dim = x.shape
    likelihoods = []
    
    for i in range(batch_size):
        likelihood = 0
        for j in range(dim):
            exponent = -0.5 * ((x[i, j] - mu[i, j]) / math.exp(log_std[j])) ** 2
            likelihood += -0.5 * math.log(2 * math.pi) - log_std[j] - exponent
        likelihoods.append(likelihood)
    
    return likelihoods