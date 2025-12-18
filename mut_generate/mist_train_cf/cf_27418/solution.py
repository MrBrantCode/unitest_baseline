"""
QUESTION:
Implement a function `build_weighted_graph(data: List[str]) -> Dict[str, List[Tuple[str, int]]]` that takes a list of strings representing rules for a weighted graph and returns a dictionary representing the weighted graph. Each rule in the input list starts with the name of a bag, followed by "bags contain", and a list of contained bags with their quantities. The dictionary should have bag names as keys and lists of tuples as values, where each tuple contains the name of a contained bag and its quantity. The function should handle rules where a bag contains "no other bags".
"""

import re
from typing import List, Dict, Tuple

def build_weighted_graph(data: List[str]) -> Dict[str, List[Tuple[str, int]]]:
    weighted_graph = {}
    root_regex = re.compile(r"([\w ]+) bags contain")
    children_regex = re.compile(r"(?:(?:(\d+) ([\w ]+)) bags?)")

    for rule in data:
        root_match = root_regex.match(rule)
        root_bag = root_match.group(1)
        children_matches = children_regex.findall(rule)

        weighted_graph[root_bag] = []
        for match in children_matches:
            if match[0] and match[1]:
                quantity = int(match[0])
                bag_name = match[1]
                weighted_graph[root_bag].append((bag_name, quantity))

    return weighted_graph