"""
QUESTION:
Write a function `rollback_to_previous_changeset` that takes a changeset number as input and returns the steps to rollback to that changeset in TFS. Assume TFS version is 2010 or later.
"""

def rollback_to_previous_changeset(changeset_number):
    """
    Returns the steps to rollback to a specific changeset in TFS.
    
    Parameters:
    changeset_number (str): The number of the changeset to rollback to. It should be prefixed with 'C'.
    
    Returns:
    list: A list of steps to rollback to the specified changeset.
    """
    
    # Check if the changeset number starts with 'C'
    if not changeset_number.startswith('C'):
        changeset_number = 'C' + changeset_number
    
    # Option 1: Through Visual Studio (steps are not implemented in code, only command line option is implemented)
    
    # Option 2: Through Command Line
    rollback_command = f"tfpt rollback /changeset:{changeset_number}"
    
    # For TFS 2012 or later
    alternative_rollback_command = f"tf rollback /changeset:{changeset_number}"
    
    return rollback_command, alternative_rollback_command