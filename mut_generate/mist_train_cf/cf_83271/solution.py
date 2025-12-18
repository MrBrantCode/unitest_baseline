"""
QUESTION:
Create a function `process_messages` that simulates a vxWorks system to process high and low priority messages from two separate queues. The function should ensure that high priority messages are processed in FIFO order, followed by low priority messages also in FIFO order. If there are no high priority messages, the function should process low priority messages immediately. Implement this function with the restriction that high priority messages should preempt low priority messages as soon as they arrive.
"""

from queue import Queue
from typing import List, Any

def process_messages(high_priority_queue: Queue, low_priority_queue: Queue) -> List[Any]:
    result = []
    
    while not high_priority_queue.empty() or not low_priority_queue.empty():
        if not high_priority_queue.empty():
            # Process high priority message
            result.append(high_priority_queue.get())
        elif not low_priority_queue.empty():
            # Process low priority message
            result.append(low_priority_queue.get())
    
    return result