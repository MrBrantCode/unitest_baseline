"""
QUESTION:
Write a function called `should_place_business_logic_in_database` that determines whether to place business logic in the database or in the application/middle tier. The function should return a boolean indicating whether the business logic should be placed in the database. Assume database independence is not a goal.
"""

def should_place_business_logic_in_database(complexity, required_performance, team_experience, database_independence_required):
    """
    This function determines whether to place business logic in the database or in the application/middle tier.
    
    Parameters:
    complexity (str): The complexity of the business logic (simple/complex)
    required_performance (str): The required performance (high/low)
    team_experience (str): The experience of the team (high/low)
    database_independence_required (bool): Whether database independence is required or not
    
    Returns:
    bool: Whether the business logic should be placed in the database
    """
    if database_independence_required:
        return False
    
    if complexity == 'simple' and required_performance == 'low' and team_experience == 'high':
        return True
    else:
        return False