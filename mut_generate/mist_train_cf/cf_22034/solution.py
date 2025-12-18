"""
QUESTION:
Calculate the conditional probability of an event occurring given a list of probabilities for each outcome, where the sum of the probabilities must equal 1. Implement a recursive function `conditional_probability` that takes a list of probabilities and the index of the event as input.
"""

def conditional_probability(probabilities, event_index):
    # Base case: If the event index is the last index, return the probability of that event
    if event_index == len(probabilities) - 1:
        return probabilities[event_index]
    
    # Recursive case: Calculate the conditional probability recursively
    else:
        return (probabilities[event_index] / (1 - sum(probabilities[event_index+1:]))) * conditional_probability(probabilities, event_index + 1)