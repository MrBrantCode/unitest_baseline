"""
QUESTION:
Write a function called `calculate_probability` that estimates the probability of an event by dividing the number of times the event occurs by the total number of trials. The function should take two parameters: `event_occurrences` (the number of times the event occurs) and `total_trials` (the total number of trials).
"""

def calculate_probability(event_occurrences, total_trials):
    """
    Estimates the probability of an event by dividing the number of times the event occurs by the total number of trials.
    
    Args:
        event_occurrences (int): The number of times the event occurs.
        total_trials (int): The total number of trials.
    
    Returns:
        float: The estimated probability of the event.
    """
    return event_occurrences / total_trials