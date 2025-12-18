"""
QUESTION:
Implement a function `update_task_document` that takes a task identifier `task_id`, a current timestamp `now`, and a timeout duration `timeout` as input. The function should update a task document with the specified `task_id` by setting "cancelled" and "orphaned" fields to `True`, updating the "end_time" field to the `now` timestamp, and updating the "result" field to a failed state with a "Timed out!" message if the difference between `now` and the task's "start_time" is greater than or equal to the `timeout`. Return the updated task document.
"""

def update_task_document(task_id: str, now: int, timeout: int, task_document: dict) -> dict:
    """
    Updates a task document with the specified task_id by setting "cancelled" and "orphaned" fields to True,
    updating the "end_time" field to the now timestamp, and updating the "result" field to a failed state 
    with a "Timed out!" message if the difference between now and the task's "start_time" is greater than 
    or equal to the timeout.

    Args:
        task_id (str): The identifier of the task.
        now (int): The current timestamp.
        timeout (int): The timeout duration.
        task_document (dict): The task document to be updated.

    Returns:
        dict: The updated task document.
    """

    if now - task_document["start_time"] >= timeout:
        task_document = {
            **task_document,
            "cancelled": True,
            "orphaned": True,
            "end_time": now,
            "result": {"state": "fail", "msg": "Timed out!"}
        }

    return task_document