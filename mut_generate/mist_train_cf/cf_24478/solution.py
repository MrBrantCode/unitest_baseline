"""
QUESTION:
Write a function called `dependency_injection` that demonstrates the concept of dependency injection. The function should take in a dependency as a parameter and use it to perform an action, showcasing the separation of an object's dependencies from its own behavior.
"""

def dependency_injection(dependency):
    """
    This function demonstrates the concept of dependency injection.
    
    Args:
    dependency (object): The dependency that will be used to perform an action.
    
    Returns:
    str: A message indicating the action performed by the dependency.
    """
    action = dependency.perform_action()
    return f"The dependency performed the action: {action}"