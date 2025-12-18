"""
QUESTION:
Write a function called 'update_ui' to describe how React.js updates the user interface. The function should explain the process React.js takes to update the UI when a user interacts with the page.
"""

def update_ui(state_change):
    """
    Describe how React.js updates the user interface.
    
    When a user interacts with the page, React.js detects the change in state and triggers a re-render.
    This means that React.js will re-run the code for the components involved and render a new user interface.
    
    Parameters:
    state_change (bool): Whether a state change has occurred.
    
    Returns:
    str: A message describing how React.js updates the UI.
    """
    if state_change:
        # React.js detects the change in state and triggers a re-render
        return "Re-rendering the page..."
    else:
        # No state change, no re-render
        return "No update needed."