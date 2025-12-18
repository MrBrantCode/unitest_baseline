"""
QUESTION:
Write a function `check_event_nature` that takes three parameters: `P_E`, `P_F`, and `P_E_and_F`, representing the probabilities of event E, event F, and the intersection of events E and F respectively. Return a string indicating the nature of the events: "independent and mutually exclusive", "neither independent nor mutually exclusive", "mutually exclusive but not independent", or "independent but not mutually exclusive" based on the conditions: events are independent if P(E ∩ F) = P(E) * P(F) and mutually exclusive if P(E ∩ F) = 0.
"""

def check_event_nature(P_E, P_F, P_E_and_F):
    # check if independent
    independent = P_E_and_F == P_E * P_F

    # check if mutually exclusive
    mutually_exclusive = P_E_and_F == 0

    if independent and mutually_exclusive:
        return "independent and mutually exclusive"
    elif not independent and not mutually_exclusive:
        return "neither independent nor mutually exclusive"
    elif mutually_exclusive and not independent:
        return "mutually exclusive but not independent"
    else:
        return "independent but not mutually exclusive"