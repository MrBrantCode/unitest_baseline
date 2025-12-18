"""
QUESTION:
Implement a function `get_distinguished_cand` that determines candidates who can become stronger than a dropped candidate `c` by adding manipulative votes, based on the strength order of candidates and non-manipulative voter rankings. The function takes the following parameters: `c` (dropped candidate index, int), `r` (number of manipulators, int), `l` (parameter of l-bloc rule, int), `non_manip_rankmaps` (preflib format for voters rankings, list of dicts), and `strength_order` (ordering of candidates according to non-manipulative votes, list). The function should return the distinguished candidates.
"""

def get_distinguished_cand(c, r, l, non_manip_rankmaps, strength_order):
    # Create a dictionary to store the strength of each candidate
    candidate_strength = {candidate: 0 for candidate in strength_order}

    # Iterate through the non-manipulative voter rankings to calculate the strength of each candidate
    for rankmap in non_manip_rankmaps:
        for candidate, rank in rankmap.items():
            candidate_strength[candidate] += 1 / rank  # Increase the strength based on the inverse of the rank

    # Sort the candidates based on their strength in descending order
    sorted_candidates = sorted(candidate_strength, key=candidate_strength.get, reverse=True)

    # Identify the potential distinguished candidates
    distinguished_candidates = []
    for candidate in sorted_candidates:
        if candidate != c and candidate_strength[candidate] > candidate_strength[c]:
            distinguished_candidates.append(candidate)

    return distinguished_candidates[:l]  # Return the top l distinguished candidates based on the l-bloc rule