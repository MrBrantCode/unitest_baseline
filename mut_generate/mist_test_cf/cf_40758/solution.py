"""
QUESTION:
Implement a method `sample_tasks` that generates a specified number of tasks for a 2D particle simulation environment. Each task should be represented as a dictionary containing task-specific parameters. The method should take an integer `num_tasks` as input and return a list of dictionaries, each representing a task with specific parameters. There are no specific bounds for the observation space, but the action space is a 2-dimensional box with bounds between -0.1 and 0.1.
"""

def sample_tasks(num_tasks):
    """
    Generate a specified number of tasks, each represented as a dictionary containing task-specific parameters.

    Parameters:
    num_tasks (int): The number of tasks to generate.

    Returns:
    list: A list of dictionaries, each representing a task with specific parameters.
    """
    tasks = []
    for _ in range(num_tasks):
        # Generate task-specific parameters
        task_params = {
            'observation_space': '2D particle simulation environment',
            'action_space': {'low': [-0.1, -0.1], 'high': [0.1, 0.1]}
            # Add more task-specific parameters as needed
        }
        tasks.append(task_params)
    return tasks