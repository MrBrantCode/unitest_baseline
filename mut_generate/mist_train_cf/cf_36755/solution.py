"""
QUESTION:
Write a Python function called `run_ml_algorithm` that takes two parameters: 
- `algorithm_name` (string): The name of the machine learning algorithm to be executed.
- `data` (any): The input data on which the algorithm will be applied.

The function should dynamically load the specified algorithm module from the `simple_ml` library, create an instance of the algorithm, and then apply it to the input data. If the specified algorithm is not available in the library, the function should return "Algorithm not found". 

Assume that the algorithm modules in the `simple_ml` library have a consistent interface for creating and applying the algorithms, specifically with a `fit` method for training.
"""

def run_ml_algorithm(algorithm_name, data):
    try:
        algorithm_module = __import__('simple_ml.' + algorithm_name, fromlist=[algorithm_name])
        algorithm_class = getattr(algorithm_module, algorithm_name.capitalize())
        algorithm_instance = algorithm_class()
        result = algorithm_instance.fit(data)  # Assuming the algorithm has a fit method for training
        return result
    except ImportError:
        return "Algorithm not found"