"""
QUESTION:
Implement a function that determines whether a state machine or a routing slip should be used to manage a workflow process. The function should take into account the linearity of the workflow sequence and the complexity of the conditional transitions. Define the function `choose_workflow_tool(linear_sequence, complex_transitions)`, where `linear_sequence` is a boolean indicating whether the workflow sequence is linear, and `complex_transitions` is a boolean indicating whether the workflow has complex conditional transitions.
"""

def choose_workflow_tool(linear_sequence, complex_transitions):
    """
    Determines whether a state machine or a routing slip should be used to manage a workflow process.

    Args:
        linear_sequence (bool): Whether the workflow sequence is linear.
        complex_transitions (bool): Whether the workflow has complex conditional transitions.

    Returns:
        str: The recommended workflow tool ("State Machine" or "Routing Slip").
    """
    if complex_transitions or not linear_sequence:
        return "State Machine"
    else:
        return "Routing Slip"