"""
QUESTION:
Write a function `quantum_superposition` that takes in a list of quantum states and returns a new list with all possible superpositions of the input states.
"""

def quantum_superposition(states):
    if not states:
        return [[]]
    
    first_state = states[0]
    rest_states = states[1:]
    
    sub_superpositions = quantum_superposition(rest_states)
    
    superpositions = []
    for sub_superposition in sub_superpositions:
        for element in first_state:
            superpositions.append([element] + sub_superposition)
    
    return superpositions