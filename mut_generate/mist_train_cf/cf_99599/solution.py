"""
QUESTION:
Create a function called `most_influential_pioneer` that takes a list of tuples as input, where each tuple contains the name of a Deep Learning pioneer and their contribution. The function should return the name of the pioneer with the most significant contribution, assuming the significance of a contribution is based on the number of people who have contributed to it.
"""

def most_influential_pioneer(pioneers):
    contributions = {}
    for pioneer, contribution in pioneers:
        if contribution in contributions:
            contributions[contribution].append(pioneer)
        else:
            contributions[contribution] = [pioneer]
    max_contribution = max(contributions.keys(), key=lambda x: len(contributions[x]))
    return contributions[max_contribution][0]