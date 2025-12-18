"""
QUESTION:
Write a function `check_scaling` that determines whether it's advisable to standardize or rescale features of a dataset based on a given machine learning algorithm. The function should take two parameters: `algorithm`, a string representing the name of the machine learning algorithm to be used, and `features`, a list of feature names. The function should return a string specifying whether to standardize, rescale, or both, and which features to apply the transformation to.

The decision should be based on the following rules:

- If the algorithm requires features to be centered around 0, the function should return 'Standardize all features'.
- If the algorithm requires features to be in the same scale, the function should return 'Rescale all features'.
- If the algorithm has no specific requirements, the function should return 'No scaling required'.
- If only some features exhibit a normal distribution, the function should still return 'Standardize all features' or 'Rescale all features' based on the algorithm's requirements, but mention that it's acceptable to standardize or rescale only the features that exhibit a normal distribution.

Note: The Shapiro-Wilk test should not be used to determine whether to standardize or rescale the features.
"""

def check_scaling(algorithm, features):
    """
    Determines whether it's advisable to standardize or rescale features of a dataset based on a given machine learning algorithm.

    Args:
        algorithm (str): The name of the machine learning algorithm to be used.
        features (list): A list of feature names.

    Returns:
        str: A string specifying whether to standardize, rescale, or both, and which features to apply the transformation to.
    """

    # Dictionary mapping algorithms to their scaling requirements
    scaling_requirements = {
        'centered_around_zero': 'Standardize all features',
        'same_scale': 'Rescale all features',
    }

    # Check if the algorithm has specific scaling requirements
    if algorithm in scaling_requirements:
        return scaling_requirements[algorithm]
    else:
        return 'No scaling required'