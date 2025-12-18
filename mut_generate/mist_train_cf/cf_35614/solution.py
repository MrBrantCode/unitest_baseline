"""
QUESTION:
Implement a function `process_data(visual_conf, rel_coll_data)` that takes a dictionary `visual_conf` and a list of dictionaries `rel_coll_data` as input. The function should return a new list containing tuples, where each tuple consists of a tag from `visual_conf` and the corresponding name from `rel_coll_data` if the tag is present in the `labels` list of any dictionary in `rel_coll_data`. The function should stop checking `rel_coll_data` for a tag once a match is found.
"""

def process_data(visual_conf, rel_coll_data):
    result = []
    for tag, description in visual_conf.items():
        for data_entry in rel_coll_data:
            if tag in data_entry.get("labels", []):
                result.append((tag, data_entry["name"]))
                break  # Once a match is found, move to the next tag
    return result