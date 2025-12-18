"""
QUESTION:
Write a function named `kl_divergence` that calculates the Kullback-Leibler (KL) divergence, a measure of the difference between the actual average activation of a neuron and a desired level of sparsity in a sparse autoencoder. The function should take as input the average activation of a neuron and the desired level of sparsity. The function should return the KL divergence value.
"""

def kl_divergence(avg_activation, desired_sparsity):
    """
    Calculate the Kullback-Leibler (KL) divergence between the average activation of a neuron 
    and a desired level of sparsity in a sparse autoencoder.

    Args:
        avg_activation (float): The average activation of a neuron.
        desired_sparsity (float): The desired level of sparsity.

    Returns:
        float: The KL divergence value.
    """
    return desired_sparsity * np.log(desired_sparsity / avg_activation) + (1 - desired_sparsity) * np.log((1 - desired_sparsity) / (1 - avg_activation))