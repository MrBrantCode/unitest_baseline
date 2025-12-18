"""
QUESTION:
Write a function `find_right_root` that identifies the correct root among multiple roots of the Maximum Likelihood (ML) function in cases where the maximum likelihood value cannot be used as a criterion to choose. The function should take as input the ML function and the roots found by the Newton-Raphson method, and should return the "right" root. The function should be able to handle cases where the correct root is not the one with the highest likelihood, and should provide a way to determine the correct root for small sample sizes.
"""

def find_right_root(ml_function, roots):
    """
    Identifies the correct root among multiple roots of the Maximum Likelihood (ML) function.
    
    Parameters:
    ml_function (function): The Maximum Likelihood function.
    roots (list): The roots found by the Newton-Raphson method.
    
    Returns:
    The "right" root that maximizes the likelihood function.
    """
    
    # Initialize the maximum likelihood and the corresponding root
    max_likelihood = float('-inf')
    right_root = None
    
    # Iterate over each root
    for root in roots:
        # Evaluate the likelihood function at the current root
        likelihood = ml_function(root)
        
        # Update the maximum likelihood and the corresponding root if necessary
        if likelihood > max_likelihood:
            max_likelihood = likelihood
            right_root = root
    
    # Return the "right" root
    return right_root