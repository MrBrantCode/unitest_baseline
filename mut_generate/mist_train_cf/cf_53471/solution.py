"""
QUESTION:
Identify the scenarios that are best suited for 'classic' state-based testing versus using mock objects. 

Consider the system's behavior, data-driven applications, stateful components, functionality and output testing, integration levels, algorithm testing, behavioral testing, isolated unit testing, testing with external dependencies, asynchronous processes, and expensive resources.
"""

def choose_testing_strategy(system_behavior, test_type, dependencies, process_type):
    """
    This function determines the best testing strategy for a given scenario.

    Args:
        system_behavior (str): The behavior of the system.
        test_type (str): The type of test.
        dependencies (list): A list of dependencies.
        process_type (str): The type of process.

    Returns:
        str: The recommended testing strategy.
    """

    # Define the testing strategies
    classic_testing = ['data-driven applications', 'stateful components', 'functionality and output testing', 
                       'integration levels', 'algorithm testing']
    mock_testing = ['behavioral testing', 'isolated unit testing', 'testing with external dependencies', 
                    'asynchronous processes', 'expensive resources']

    # Check if system behavior is suitable for classic testing
    if system_behavior.lower() in classic_testing:
        return "Classic (State-Based) Testing"

    # Check if test type is suitable for mock testing
    elif test_type.lower() in mock_testing:
        return "Mock Object Testing"

    # Check if dependencies or process type require mock testing
    elif dependencies or process_type.lower() in ['asynchronous processes', 'expensive resources']:
        return "Mock Object Testing"

    # Default to classic testing
    else:
        return "Classic (State-Based) Testing"