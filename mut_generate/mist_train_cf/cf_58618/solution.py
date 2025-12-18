"""
QUESTION:
Create a function to generate a list of checkboxes for selecting environments where a bug was found in Azure DevOps, with the ability to select multiple environments for a single work item. 

The function should be able to return a list or data structure that can be used to create this multi-select checkbox control, considering the current limitations of Azure DevOps where custom fields and tags can only be used for single selection.
"""

def generate_environment_checkboxes(environments):
    """
    Generate a list of checkboxes for selecting environments where a bug was found in Azure DevOps.
    
    Args:
        environments (list): A list of environment names.
    
    Returns:
        list: A list of dictionaries representing checkboxes.
    """
    checkboxes = []
    for environment in environments:
        checkboxes.append({
            'name': environment,
            'checked': False  # default to unchecked
        })
    return checkboxes