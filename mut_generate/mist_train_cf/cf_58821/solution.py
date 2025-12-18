"""
QUESTION:
Implement a function `choose_database` that takes as input the project size (`small`, `medium`, or `large`), budget (`low`, `medium`, or `high`), and priority (`security`, `scalability`, or `simplicity`) and returns the recommended database type (`commercial`, `open_source`, `NoSQL`, or `cloud`).
"""

def choose_database(project_size, budget, priority):
    """
    Recommends a database type based on project size, budget, and priority.

    Args:
    project_size (str): The size of the project (small, medium, or large).
    budget (str): The budget for the project (low, medium, or high).
    priority (str): The priority of the project (security, scalability, or simplicity).

    Returns:
    str: The recommended database type (commercial, open_source, NoSQL, or cloud).
    """

    # Define a dictionary to store the database recommendations
    database_recommendations = {
        'small': {'low': 'open_source', 'medium': 'open_source', 'high': 'commercial'},
        'medium': {'low': 'open_source', 'medium': 'NoSQL', 'high': 'commercial'},
        'large': {'low': 'NoSQL', 'medium': 'NoSQL', 'high': 'commercial'}
    }

    # Define a dictionary to store the priority-based recommendations
    priority_recommendations = {
        'security': 'commercial',
        'scalability': 'cloud',
        'simplicity': 'open_source'
    }

    # First, check if the project size and budget combination has a specific recommendation
    if project_size in database_recommendations and budget in database_recommendations[project_size]:
        recommended_database = database_recommendations[project_size][budget]
    # If not, check if the priority has a specific recommendation
    elif priority in priority_recommendations:
        recommended_database = priority_recommendations[priority]
    # If none of the above conditions are met, default to open_source
    else:
        recommended_database = 'open_source'

    return recommended_database