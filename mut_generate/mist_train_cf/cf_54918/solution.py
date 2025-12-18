"""
QUESTION:
Implement a function `polynomial_regression_analysis` that takes in parameters for polynomial degree, method of learning weights (either 'matrix_inversion' or 'gradient_descent'), assumed variance of Gaussian noise, and whether to include a constant-term unit input. The function should return an analysis of how these parameters influence the delicate balance between underfitting and overfitting in polynomial regression.
"""

def polynomial_regression_analysis(degree, method, variance, constant_term):
    """
    Analyze the influence of polynomial degree, method of learning weights, 
    assumed variance of Gaussian noise, and constant-term unit input on 
    the delicate balance between underfitting and overfitting in polynomial regression.

    Parameters:
    degree (int): The degree of the polynomial.
    method (str): The method of learning weights. Either 'matrix_inversion' or 'gradient_descent'.
    variance (float): The assumed variance of Gaussian noise.
    constant_term (bool): Whether to include a constant-term unit input.

    Returns:
    str: An analysis of how the parameters influence the balance between underfitting and overfitting.
    """
    
    analysis = "The polynomial degree of " + str(degree) + " may cause "
    if degree < 2:
        analysis += "underfitting by oversimplifying the problem. "
    elif degree > 5:
        analysis += "overfitting by capturing not only the pattern but also the noise in the data. "
    else:
        analysis += "a good balance between underfitting and overfitting. "

    analysis += "The method of learning weights is " + method + ". "
    if method == 'matrix_inversion':
        analysis += "Matrix inversion can be more computationally intensive, but finds the solution in one go. "
    elif method == 'gradient_descent':
        analysis += "Gradient descent is an iterative approach that gradually descends towards the minimum of the error surface. "

    analysis += "The assumed variance of Gaussian noise is " + str(variance) + ". "
    if variance < 0.1:
        analysis += "A low variance may not capture the noise in the data, resulting in underfitting. "
    elif variance > 10:
        analysis += "A high variance may capture too much noise, resulting in overfitting. "

    analysis += "The utilisation of a constant-term unit input is " + str(constant_term) + ". "
    if constant_term:
        analysis += "This can be useful to account for the base level of the dependent variable when all predictors are zero. "
    else:
        analysis += "This assumes the line fitted goes through the origin. "

    return analysis