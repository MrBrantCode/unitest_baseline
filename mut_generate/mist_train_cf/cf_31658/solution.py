"""
QUESTION:
Write a function `generate_graph_vector(ent1_vector, rel_vector, ent2_vector, lens, case_id)` that takes in the following parameters:
- `ent1_vector`: A numpy array representing the entity 1 vector.
- `rel_vector`: A numpy array representing the relation vector.
- `ent2_vector`: A numpy array representing the entity 2 vector.
- `lens`: A scalar value representing the length for normalization.
- `case_id`: A unique identifier for the graph vector.

The function should return a dictionary `graph_vector` containing the graph vector for the given `case_id`. Assume that the input numpy arrays (`ent1_vector`, `rel_vector`, `ent2_vector`) are of the same length and the `case_id` is unique.
"""

import numpy as np

def generate_graph_vector(ent1_vector, rel_vector, ent2_vector, lens, case_id):
    ent2_vector = np.array(ent2_vector / lens)
    vector = np.concatenate((ent1_vector, rel_vector, ent2_vector), axis=-1)
    graph_vector = {case_id: vector}
    return graph_vector