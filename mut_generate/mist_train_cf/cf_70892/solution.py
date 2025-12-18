"""
QUESTION:
Implement a function named `reject_previous_run` that automatically rejects the previous run in a continuous integration and continuous delivery pipeline when a new run is initiated. The function should take the current run ID and a list of pending run IDs as input, and return a list of run IDs that are still pending after rejecting the previous run. The function should assume that each new run is initiated with a unique run ID and that the list of pending run IDs is ordered by initiation time, with the most recent run ID last.
"""

def reject_previous_run(current_run_id, pending_run_ids):
    """
    Rejects the previous run in a continuous integration and continuous delivery pipeline 
    when a new run is initiated.

    Args:
    current_run_id (int): The ID of the current run.
    pending_run_ids (list): A list of pending run IDs, ordered by initiation time.

    Returns:
    list: A list of run IDs that are still pending after rejecting the previous run.
    """
    if pending_run_ids and pending_run_ids[-1] != current_run_id:
        pending_run_ids[-1] = current_run_id
    return pending_run_ids