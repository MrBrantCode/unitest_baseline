"""
QUESTION:
Create a function named `load_worker` that takes a string parameter `worker_class` representing the fully qualified name of a worker class, loads the class dynamically, instantiates it, calls its `execute_task` method, and returns the result. Assume the `execute_task` method takes no arguments and returns a string.
"""

import importlib

def load_worker(worker_class):
    """
    Dynamically loads a worker class, instantiates it, calls its execute_task method, and returns the result.

    Args:
    worker_class (str): The fully qualified name of the worker class.

    Returns:
    str: The result of the execute_task method.
    """

    # Split the fully qualified class name to get the module and class names
    module_name, class_name = worker_class.rsplit('.', 1)

    # Dynamically import the module
    module = importlib.import_module(module_name)

    # Get the worker class from the imported module
    worker_class = getattr(module, class_name)

    # Instantiate the worker class
    worker_instance = worker_class()

    # Call the execute_task() method and return the output
    return worker_instance.execute_task()