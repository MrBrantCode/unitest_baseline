"""
QUESTION:
Write a function named `find_reachable_states` that takes three parameters: `N`, `M`, and `transitions`. `N` is an integer representing the number of states in the DFA (1 ≤ N ≤ 10^5), `M` is an integer representing the number of symbols in the input alphabet (1 ≤ M ≤ 26), and `transitions` is a 2D array of size N x M representing the transition function of the DFA. The function should return three sets: `reachable_states`, `non_reachable_states`, and `partially_reachable_states`, representing the states that are reachable from the initial state, the states that are not reachable from the initial state, and the states that are partially reachable from the initial state, respectively. The function should have a time complexity of O(N + M) and a space complexity of O(N), where N is the number of states and M is the number of symbols in the input alphabet. The initial state of the DFA is always assumed to be state 0. The `reachable_states`, `non_reachable_states`, and `partially_reachable_states` sets should not contain duplicate elements.
"""

def find_reachable_states(N, M, transitions):
    reachable_states = set([0])  # Initialize reachable_states with the initial state
    stack = [0]  # Initialize stack with the initial state

    while stack:
        state = stack.pop()

        for symbol in range(M):
            next_state = transitions[state][symbol]

            if next_state not in reachable_states:
                reachable_states.add(next_state)
                stack.append(next_state)

    non_reachable_states = set()
    for state in range(N):
        if state not in reachable_states:
            non_reachable_states.add(state)

    partially_reachable_states = set()
    for state in range(N):
        if state in reachable_states and state not in non_reachable_states:
            partially_reachable_states.add(state)

    return reachable_states, non_reachable_states, partially_reachable_states