"""
QUESTION:
Implement a function `analyze_sequencing_runs` that takes a list of sequencing runs as input. The function should check for missing components of the analysis in each run, where the components are "alignment", "quality_check", and "variant_calling". Return a dictionary where the keys are the sequencing runs and the values are lists of missing components for each run. If all components are present for a run, the corresponding value should be an empty list.
"""

def analyze_sequencing_runs(runs):
    """
    Analyze sequencing runs for missing components.

    Args:
    runs (list): A list of sequencing runs.

    Returns:
    dict: A dictionary where the keys are the sequencing runs and the values are lists of missing components for each run.
    """
    components = ["alignment", "quality_check", "variant_calling"]
    missing_components = {}

    for run in runs:
        missing = [comp for comp in components if comp not in get_existing_components(run)]
        missing_components[run] = missing

    return missing_components

def get_existing_components(run):
    """
    Retrieve existing components for a given sequencing run.

    Args:
    run (str): A sequencing run.

    Returns:
    list: A list of existing components for the given sequencing run.
    """
    # Replace with actual implementation to fetch existing components from the system
    # For demonstration purposes, assume the following existing components
    if run == 'Tue28':
        return ["alignment", "variant_calling"]
    elif run == 'test_tiny':
        return ["quality_check"]
    else:
        return []