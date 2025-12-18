"""
QUESTION:
Create a function `calculate_diff(container1, container2)` that takes two containers (e.g., folders, URLs, files, strings) as input and returns two lists: `added` and `removed`. The `added` list should contain elements that are present in `container2` but not in `container1`, and the `removed` list should contain elements that are present in `container1` but not in `container2`. The function should use only the two input containers and not create any additional containers with the original elements. The elements in the containers are hashable and comparable, but may not contain duplicate elements.
"""

def calculate_diff(container1, container2):
    # creating hash maps for the two containers
    map1 = {i : 1 for i in container1}
    map2 = {i : 1 for i in container2}
    
    # calculating added and removed elements
    added = [i for i in map2 if i not in map1]
    removed = [i for i in map1 if i not in map2]
    
    return added, removed