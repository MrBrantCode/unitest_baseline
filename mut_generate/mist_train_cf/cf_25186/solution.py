"""
QUESTION:
Write a Python function `join_sets` that takes four lists as input: `user_id1`, `firstname`, `user_id2`, and `lastname`. The function should join the two sets based on the `user_id` and create a new set with `firstname`, `lastname`, and `user_id`. The resulting set should contain only the `user_id` values that are common to both input sets.
"""

def join_sets(user_id1, firstname, user_id2, lastname):
    result = []
    common_ids = set(user_id1) & set(user_id2)
    for id in common_ids:
        id_index1 = user_id1.index(id)
        id_index2 = user_id2.index(id)
        result.append({"user_id": id, "firstname": firstname[id_index1], "lastname": lastname[id_index2]})
    return result