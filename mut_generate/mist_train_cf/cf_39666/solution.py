"""
QUESTION:
Write a Python function called `analyze_profiling_results` that takes a file path to profiling results as input and returns a list of tuples containing the function name and its corresponding cumulative time. The function should use the `pstats` module to analyze the profiling results, sort them based on cumulative time, and return the top results.
"""

import pstats

def analyze_profiling_results(file_path):
    """
    Analyze profiling results from a file and return a list of tuples containing 
    the function name and its corresponding cumulative time.

    Args:
    file_path (str): The path to the profiling results file.

    Returns:
    list: A list of tuples containing the function name and its cumulative time.
    """
    stats = pstats.Stats(file_path)
    stats.strip_dirs()
    stats.sort_stats("cumulative")
    return stats.stats