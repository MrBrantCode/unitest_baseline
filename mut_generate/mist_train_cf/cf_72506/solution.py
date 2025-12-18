"""
QUESTION:
Create a function `calculate_balance_score` and `suggest_improvements` for a remote worker with the given parameters: work hours, breaks, productivity level, leisure time, sleep hours, and health stats. The `calculate_balance_score` function should calculate a balance score based on work hours, health, and productivity levels. The `suggest_improvements` function should suggest improvements if the worker's work hours exceed 8 hours, sleep hours are less than 8 hours, or leisure time is less than 2 hours. The balance score should be considered good if it is above 0.6. 

Restrictions: The input parameters should be numeric values and the output should be a numeric balance score and a list of suggestions.
"""

def calculate_balance_score(work_hours, health, productivity):
    """
    Calculate a balance score based on work hours, health, and productivity levels.
    
    Parameters:
    work_hours (float): The number of hours worked.
    health (float): The health stats of the worker.
    productivity (float): The productivity level of the worker.
    
    Returns:
    float: The balance score.
    """
    work_balance = work_hours / (work_hours + 8) # assuming 8 hours of leisure and sleep time
    health_bonus = health / 100.0
    productivity_bonus = productivity / 100.0
    balance_score = (work_balance + health_bonus + productivity_bonus) / 3.0
    return balance_score


def suggest_improvements(work_hours, sleep, leisure):
    """
    Suggest improvements if the worker's work hours exceed 8 hours, sleep hours are less than 8 hours, or leisure time is less than 2 hours.
    
    Parameters:
    work_hours (float): The number of hours worked.
    sleep (float): The number of hours slept.
    leisure (float): The number of hours of leisure time.
    
    Returns:
    list: A list of suggestions for improvement.
    """
    suggestions = []
    if work_hours > 8: 
      suggestions.append('Reduce work hours')
    if sleep < 8: 
      suggestions.append('Increase sleep hours')
    if leisure < 2: 
      suggestions.append('Need more leisure time')
    return suggestions