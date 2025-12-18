"""
QUESTION:
Predict the type of problem for a company's product sales prediction based on customer attributes.

Function name: DetermineProblemType

Information: The company has collected data from 1000 customers, including age, income, location, and whether they bought the product. The company wants to predict sales of a new product based on these customer attributes.

Restriction: The problem should be categorized as either a classification or a regression problem based on the nature of the target variable (sales).
"""

def determine_problem_type(target_variable):
    """
    Determine the type of problem (classification or regression) based on the nature of the target variable.

    Args:
        target_variable (str): The name of the target variable.

    Returns:
        str: The type of problem (classification or regression).
    """

    # In this case, the target variable is 'sales', which is a continuous numerical variable.
    if target_variable.lower() == 'sales':
        return 'regression'
    else:
        # For other target variables, you can add more conditions to determine the problem type.
        pass