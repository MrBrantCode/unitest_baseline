"""
QUESTION:
Create a function `get_attitude(name, attitude_sequence)` that takes a name and an attitude sequence as input and returns the attitude of the individual with the given name if the attitude sequence matches their attitude. The function should use a dictionary `attitudes` where each key is a unique name and the corresponding value is a list of three logical words representing the individual's attitude. The function should return an error message if the name is not in the dictionary or if the attitude sequence does not match the individual's attitude.
"""

def get_attitude(name, attitude_sequence):
    # Create a dictionary of attitudes
    attitudes = {
        "John": ["happy", "confident", "optimistic"],
        "Jane": ["sad", "anxious", "pessimistic"],
        "Bob": ["angry", "frustrated", "hopeless"]
    }
    
    # Check if the name exists in the dictionary
    if name in attitudes:
        # Check if the attitude sequence matches the individual's attitude
        if attitudes[name] == attitude_sequence:
            return "The attitude of " + name + " is " + ", ".join(attitude_sequence)
        else:
            return "The attitude sequence does not match the attitude of " + name
    else:
        return "The name is not in the dictionary"