"""
QUESTION:
Implement a function `detect_cycle(commands: List[str]) -> List[str]` to detect the first cycle in a directed graph represented as a list of commands. Each command represents a directed edge from one node to another, and is in the format "cycletest source destination". The function should return a list of commands that form the first cycle found. If no cycle is found, return an empty list.
"""

from typing import List

def detect_cycle(commands: List[str]) -> List[str]:
    graph = {}
    for command in commands:
        if command.startswith("cycletest"):
            _, source, destination = command.split()
            if source in graph:
                if destination in graph[source]:
                    return [f"cycletest {source}", f"cycletest {destination}"]
            else:
                graph[source] = set()
            graph[source].add(destination)
    return []