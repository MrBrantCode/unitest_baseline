"""
QUESTION:
Implement a recursive function `calculate_conditional_probability` that calculates the conditional probability of an event occurring given a list of outcomes, where each outcome is represented by a tuple containing the outcome and its probability. The function takes two parameters: `outcomes` (a list of tuples) and `event` (a string representing the event). The function should return the conditional probability of the event occurring, calculated by summing the probabilities of all outcomes where the event occurs and dividing it by the total probability of all outcomes. The function should handle edge cases correctly, including when the outcomes list is empty or when the event does not occur in any outcome.
"""

def calculate_conditional_probability(outcomes, event):
    # Base case: if outcomes list is empty, return 0
    if len(outcomes) == 0:
        return 0
    
    # Base case: if event does not occur in any outcome, return 0
    if event not in [outcome[0] for outcome in outcomes]:
        return 0
    
    # Initialize variables
    total_prob = 0.0
    event_prob = 0.0
    
    # Iterate over outcomes list
    for i, outcome in enumerate(outcomes):
        outcome_event = outcome[0]
        outcome_prob = outcome[1]
        
        # Check if outcome matches the event
        if outcome_event == event:
            event_prob += outcome_prob
            
        total_prob += outcome_prob
        
        # Recursive call with remaining outcomes
        if i < len(outcomes) - 1:
            remaining_outcomes = outcomes[i+1:]
            conditional_prob = calculate_conditional_probability(remaining_outcomes, event)
            event_prob += outcome_prob * conditional_prob
            
    # Calculate and return conditional probability
    return event_prob / total_prob