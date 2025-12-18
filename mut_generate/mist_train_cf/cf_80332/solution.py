"""
QUESTION:
Create a function `checkin_policy` that enforces a constraint to check if a file checked into Team Foundation Server (TFS) or Azure DevOps is associated with a work item. The function should be able to be integrated into TFS or Azure DevOps as a custom check-in policy. The policy should raise an alert when a file is checked in without being associated with a work item. 

Note: The function should be written in .NET and packaged into a VSIX extension for Visual Studio.
"""

def checkin_policy(changes, work_items):
    """
    This function checks if each change has a work item associated with it.
    
    Args:
    changes (list): A list of changes being checked in.
    work_items (list): A list of work items associated with the changes.
    
    Returns:
    bool: True if each change has a work item associated with it, False otherwise.
    """
    
    # Create a dictionary to store the changes and their associated work items
    change_work_items = {}
    
    # Iterate over the changes and their associated work items
    for change in changes:
        # Initialize an empty list for each change in the dictionary
        change_work_items[change] = []
        
    for work_item in work_items:
        # Iterate over the changes and add the work items to the corresponding change in the dictionary
        for change in changes:
            if work_item.change_id == change.id:
                change_work_items[change].append(work_item)
    
    # Check if each change has a work item associated with it
    for change in changes:
        if len(change_work_items[change]) == 0:
            # If a change does not have a work item associated with it, return False
            return False
            
    # If all changes have a work item associated with them, return True
    return True