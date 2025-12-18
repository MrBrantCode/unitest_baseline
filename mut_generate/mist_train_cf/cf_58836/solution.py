"""
QUESTION:
Write a function named `message_ordering` that explains how idempotent producer feature in Kafka helps maintain message order when a message fails and is retried. Assume each message has a Position ID (PID) and sequence number, and the Kafka broker keeps track of these sequence numbers for each PID. The function should describe how the broker ensures the messages are written in order to the log according to these sequence numbers, even if a message is retried.
"""

def message_ordering(messages):
    """
    Simulates how idempotent producer feature in Kafka maintains message order.

    Args:
        messages (list): A list of tuples containing message details (PID, sequence number, status).
        
    Returns:
        list: Messages in the order they should be written to the log.
    """
    
    # Initialize an empty log and a dictionary to keep track of sequence numbers for each PID
    log = []
    sequence_numbers = {}

    # Iterate over each message
    for message in messages:
        pid, sequence_number, _ = message
        
        # If the PID is not in the dictionary, add it with the current sequence number
        if pid not in sequence_numbers:
            sequence_numbers[pid] = sequence_number
        # If the sequence number is not consecutive, wait for the previous message to be committed
        elif sequence_numbers[pid] + 1 != sequence_number:
            continue
        # Commit the message to the log and update the sequence number for the PID
        log.append(message)
        sequence_numbers[pid] = sequence_number

    return log