"""
QUESTION:
Write a Python function `programming_paradigm_selector` that takes two parameters: `project_size` (a string representing the size of the project, either 'small' or 'large') and `performance_critical` (a boolean indicating whether performance is critical). The function should return the recommended programming paradigm ('OOP' or 'procedural') based on the project size and performance requirements.
"""

def programming_paradigm_selector(project_size: str, performance_critical: bool) -> str:
    """
    Selects the recommended programming paradigm based on project size and performance requirements.

    Args:
    project_size (str): The size of the project, either 'small' or 'large'.
    performance_critical (bool): Whether performance is critical.

    Returns:
    str: The recommended programming paradigm, either 'OOP' or 'procedural'.
    """

    # If the project is large, OOP is preferred due to its benefits in code organization, reusability, and maintainability
    if project_size == 'large':
        return 'OOP'
    
    # For small projects, if performance is critical, procedural programming is preferred due to its simplicity and efficiency
    elif project_size == 'small' and performance_critical:
        return 'procedural'
    
    # For small projects where performance is not critical, OOP can still be used due to its benefits in code organization and reusability
    else:
        return 'OOP'