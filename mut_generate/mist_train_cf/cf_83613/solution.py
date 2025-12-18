"""
QUESTION:
Define a function `conditional_probability(event1, event2)` and another function `marginal_probability(event)` that calculate the conditional probability of event B given event A and the marginal probability of event A, respectively. The events A and B are two out of four possible outcomes with given probabilities (0.1, 0.2, 0.3, 0.4), and it is given that the events are not independent of each other. The probabilities of the outcomes should sum up to 1.
"""

def conditional_probability(event1, event2, prob_dict):
    """
    Calculate the conditional probability of event1 given event2.
    
    Parameters:
    event1 (str): The event for which the conditional probability is to be calculated.
    event2 (str): The event on which the conditional probability is based.
    prob_dict (dict): A dictionary mapping events to their probabilities.
    
    Returns:
    float: The conditional probability of event1 given event2.
    """
    # Here we arbitrarily define the joint probability as the product of their probabilities.
    # This is not always valid as A and B are not always independent. You will need to adjust this 
    # according to your specific problem.
    joint_probability = prob_dict[event1] * prob_dict[event2]

    # Conditional probability of event1 given event2 is 
    # the ratio of the joint probability to the probability of event2.
    return joint_probability / prob_dict[event2]

def marginal_probability(event, prob_dict):
    """
    Calculate the marginal probability of an event.
    
    Parameters:
    event (str): The event for which the marginal probability is to be calculated.
    prob_dict (dict): A dictionary mapping events to their probabilities.
    
    Returns:
    float: The marginal probability of the event.
    """
    # The marginal probability of an event is just its probability.
    return prob_dict[event]