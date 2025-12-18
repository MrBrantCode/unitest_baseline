"""
QUESTION:
Implement a function named `process_markers` that takes a list of strings representing processed markers. The function should return a tuple containing a dictionary where keys are unique markers and values are their counts, an updated list of processed markers, and a dictionary specifying the action to be performed for each marker. The action should be 'process' if the count of a marker is 3 or more, and 'ignore' otherwise.
"""

from typing import List, Dict, Tuple

def process_markers(marker_list: List[str]) -> Tuple[Dict[str, int], List[str], Dict[str, str]]:
    marker_dict = {}
    for marker in marker_list:
        if marker in marker_dict:
            marker_dict[marker] += 1
        else:
            marker_dict[marker] = 1
    
    updated_marker_list = list(marker_dict.keys())
    
    action = {marker: 'process' if count >= 3 else 'ignore' for marker, count in marker_dict.items()}
    
    return marker_dict, updated_marker_list, action