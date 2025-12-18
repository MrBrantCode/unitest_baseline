"""
QUESTION:
Write a function called `estimate_anova_parameters` to estimate the parameters of a variance analysis model with one factor with K categories. The function should take a 2D list of observations where each inner list represents a category and return a list of estimated parameters. Each category has a mean (μ) and a variance (σ^2), but the model assumes homogeneity of variances, meaning all categories have the same variance σ^2. The function should not use any external libraries or built-in statistical functions.
"""

def estimate_anova_parameters(categories):
    """
    Estimate the parameters of a variance analysis model with one factor with K categories.

    Parameters:
    categories (list of lists): 2D list of observations where each inner list represents a category

    Returns:
    list: A list of estimated parameters, including the overall mean, group means, and shared variance
    """

    # Calculate the overall mean
    overall_mean = sum(sum(category) for category in categories) / sum(len(category) for category in categories)

    # Calculate the group means
    group_means = [sum(category) / len(category) for category in categories]

    # Calculate the shared variance
    shared_variance = sum(sum((x - group_mean) ** 2 for x in category) for category, group_mean in zip(categories, group_means)) / sum(len(category) for category in categories)

    # Calculate the overall mean as the mean of the group means
    overall_mean = sum(group_means) / len(group_means)

    return [overall_mean] + group_means + [shared_variance]