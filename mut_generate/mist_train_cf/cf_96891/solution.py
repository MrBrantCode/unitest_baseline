"""
QUESTION:
Implement a recursive function `conditional_probability(probabilities, event_index)` that calculates the conditional probability of an event at `event_index` occurring given a list of probabilities `probabilities`, where the sum of all probabilities must be equal to 1. The function should use Bayes' theorem and return the conditional probability.
"""

def conditional_probability(probabilities, event_index):
    # Base case: If the event index is the last index, return the probability of that event
    if event_index == len(probabilities) - 1:
        return probabilities[event_index]
    
    # Recursive case: Calculate the conditional probability recursively
    else:
        return (probabilities[event_index] / (1 - sum(probabilities[event_index+1:]))) * conditional_probability(probabilities, event_index + 1)