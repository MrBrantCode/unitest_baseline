"""
QUESTION:
Implement a generator function `single_generator` that takes an initial state, a goal state, a set of operators, and a successors function as input. The function should yield valid states that can be reached from the initial state using the provided operators until the goal state is reached. The generator should stop yielding states once the goal state is reached. The function should have the following signature: `def single_generator(initial, goal, operators, successors):`.
"""

def single_generator(initial, goal, operators, successors):
    visited = set()  # To keep track of visited states
    stack = [(initial, [])]  # Stack to store states and their paths

    while stack:
        state, path = stack.pop()
        if state == goal:
            yield path + [state]  # Yield the path to the goal state
            return  # Stop the generator once the goal state is reached

        if state not in visited:
            visited.add(state)
            for operator in operators:
                new_state = operator(state)
                if new_state is not None and successors(new_state):
                    stack.append((new_state, path + [state]))  # Add the new state and its path to the stack