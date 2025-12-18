"""
QUESTION:
Create a function called `separate_code_layers` that determines whether to separate code into different layers using class library projects or keep it in a single web application. The function should consider factors such as separation of concerns, modularity, testing, potential for reusability, refactoring, and maintenance when making this decision. The input to the function should include the project size, the need for unit testing, and the potential for future reuse of code. The function should return a boolean value indicating whether to separate the code into different layers or not.
"""

def separate_code_layers(project_size, need_unit_testing, potential_reuse):
    """
    Determines whether to separate code into different layers using class library projects or keep it in a single web application.
    
    Parameters:
    project_size (str): The size of the project. It can be 'small', 'medium', or 'large'.
    need_unit_testing (bool): Whether unit testing is required.
    potential_reuse (bool): Whether there's potential for future reuse of code.
    
    Returns:
    bool: Whether to separate the code into different layers or not.
    """
    
    # For small projects, it might be overkill to separate the code
    if project_size == 'small':
        return False
    
    # If unit testing is required, it's better to separate the code
    if need_unit_testing:
        return True
    
    # If there's potential for future reuse of code, it's better to separate the code
    if potential_reuse:
        return True
    
    # For medium or large projects with no other factors, it's still a good practice to separate the code
    return True