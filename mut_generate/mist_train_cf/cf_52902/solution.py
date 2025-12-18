"""
QUESTION:
Given a numpy array dL/dY representing the derivatives of the loss with respect to the output of a layer, calculate dL/dB, the derivatives of the loss with respect to the bias terms of that layer. The function should take dL/dY as input and return dL/dB.
"""

def calculate_dLdB(dLdY):
    """
    Calculate the derivatives of the loss with respect to the bias terms of a layer.
    
    Parameters:
    dLdY (numpy array): The derivatives of the loss with respect to the output of a layer.
    
    Returns:
    numpy array: The derivatives of the loss with respect to the bias terms of the layer.
    """
    return np.sum(dLdY, axis=0)