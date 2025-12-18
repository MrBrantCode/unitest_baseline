"""
QUESTION:
Write a function `extract_base_names(joint_names)` that takes a list of joint names, extracts the unique base names (the first word in each joint name, separated by underscores), and returns them in a sorted order. The function should be able to handle a list of strings and return a list of unique base names in lexicographical order.
"""

from typing import List

def extract_base_names(joint_names: List[str]) -> List[str]:
    base_names = set()
    for joint_name in joint_names:
        base_name = joint_name.split('_')[0]
        base_names.add(base_name)
    return sorted(list(base_names))