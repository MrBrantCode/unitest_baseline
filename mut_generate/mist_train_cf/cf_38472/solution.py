"""
QUESTION:
Create a class `ThreadManager` with the following methods:

- `create_thread(title: str, content: str) -> int`: Create a new thread with the given `title` and `content` and return the unique thread ID assigned.
- `reply_to_thread(thread_id: int, content: str) -> bool`: Reply to an existing thread specified by its `thread_id` and return `True` if successful, `False` otherwise.
- `get_stats() -> dict`: Return a dictionary containing thread statistics with keys `total_threads`, `total_replies`, and `average_replies_per_thread`, where `average_replies_per_thread` is rounded to two decimal places.

The class should maintain a unique thread ID that increments with each new thread created, starting from 1. If no threads have been created, the average replies per thread should be 0.
"""

def entrance(title: str, content: str) -> int:
    thread_id = entrance.next_thread_id
    entrance.threads[thread_id] = {'title': title, 'content': content, 'replies': []}
    entrance.next_thread_id += 1
    return thread_id

entrance.threads = {}
entrance.next_thread_id = 1
entrance.total_replies = 0