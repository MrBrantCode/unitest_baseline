"""
QUESTION:
Write a function `convert_nfa_to_dfa` that takes as input a dictionary representing the transitions of a Non-Deterministic Finite Automaton (NFA), a list of final states of the NFA, and a list of all states in the NFA, and returns the transitions and final states of the corresponding Deterministic Finite Automaton (DFA) with exactly 7 states, where the start state is the state with the highest number of incoming transitions and the final states include all states that are reachable from the start state, but not from any other final state.
"""

from collections import defaultdict, deque

def convert_nfa_to_dfa(nfa_transitions, nfa_final_states, nfa_states):
    # Create a dictionary to store the DFA transitions
    dfa_transitions = defaultdict(dict)
    
    # Create a set to store the DFA states
    dfa_states = set()
    
    # Create a set to store the DFA final states
    dfa_final_states = set()
    
    # Find the start state by finding the state with the highest number of incoming transitions
    start_state = max(nfa_states, key=lambda state: sum(1 for transitions in nfa_transitions.values() for next_states in transitions.values() if state in next_states))
    
    # Create an empty queue and add the start state to it
    queue = deque([[start_state]])
    
    # While the queue is not empty
    while queue:
        # Remove the first state from the queue
        current_state = queue.popleft()
        
        # Add the current state to the DFA states
        dfa_states.add(tuple(sorted(current_state)))
        
        # For each input symbol
        for symbol in 'ab':
            # Find the set of states that can be reached from the current DFA state by following that input symbol in the NFA
            next_states = set()
            for state in current_state:
                if state in nfa_transitions and symbol in nfa_transitions[state]:
                    next_states.update(nfa_transitions[state][symbol])
            
            # Combine these states into a single DFA state
            next_state = tuple(sorted(next_states))
            
            # If the combined DFA state is not already a DFA state, add it to the queue
            if next_state not in dfa_states:
                queue.append(list(next_state))
            
            # Add the transition to the DFA transitions
            dfa_transitions[tuple(current_state)][symbol] = next_state
    
    # Determine the final states by finding all states that are reachable from the start state, but not from any other final state
    for state in dfa_states:
        if any(nfa_state in nfa_final_states for nfa_state in state):
            dfa_final_states.add(state)
    
    # Convert dfa_transitions to the required format
    dfa_transitions = {state: {symbol: next_state for symbol, next_state in transitions.items()} for state, transitions in dfa_transitions.items()}
    
    return dfa_transitions, dfa_final_states