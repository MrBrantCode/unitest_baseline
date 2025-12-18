"""
QUESTION:
Write a function `update_acc(initial_points_acc, environment_acc)` where:
- initial_points_acc is a dictionary representing the initial "acc" attributes of points with keys 'S', 'E', 'M' and their corresponding accelerations as values.
- environment_acc is a dictionary representing the "acc" attribute of the environment with keys 'S', 'E', 'M' and their corresponding accelerations as values.

The function should return a dictionary representing the final "acc" attributes of the points after the update process is applied. The update process involves a series of intermediate calculations based on the initial points and environment accelerations.
"""

def update_acc(initial_points_acc, environment_acc):
    pS = {'S': initial_points_acc['S'], 'E': 0, 'M': 0}
    pQ = {'S': 0, 'E': initial_points_acc['E'], 'M': 0}
    pE = {'S': 0, 'E': 0, 'M': initial_points_acc['M']}
    pM = {'S': 0, 'E': 0, 'M': 0}

    pQ['S'] = environment_acc['S'] + pQ['S']
    pQ['E'] = environment_acc['E'] + pQ['E']
    pQ['M'] = environment_acc['M'] + pM['M']

    pS['S'] = pQ['S'] + pS['S']
    pS['E'] = pQ['E'] + pE['E']
    pS['M'] = pE['M'] + pM['M']

    return {'S': pS['S'], 'E': pS['E'], 'M': pS['M']}