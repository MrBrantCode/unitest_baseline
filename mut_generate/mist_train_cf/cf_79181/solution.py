"""
QUESTION:
Create a function `find_oldest_with_trait` that uses a binary search tree to find the oldest dwarf with a specific character trait from a given dictionary of dwarfs, where each dwarf has a unique age and a list of traits. The time complexity of the function should be no worse than O(log n), where n is the number of dwarfs. The function should take two parameters: the root of the binary search tree and the target trait. The function should return the age of the oldest dwarf with the target trait if found, otherwise it should return None.
"""

class Node: 
    def __init__(self, data, traits): 
        self.left = None
        self.right = None
        self.data = data
        self.traits = traits

def add_node(root, data, traits): 
    if root is None: 
        return Node(data, traits) 
    else: 
        if root.data < data: 
            root.right = add_node(root.right, data, traits) 
        else: 
            root.left = add_node(root.left, data, traits) 
    return root

def find_oldest_with_trait(root, trait): 
    if root is None or root.traits is None: 
        return None
    right = find_oldest_with_trait(root.right, trait) 
    if right is not None: 
        return right 
    if trait in root.traits: 
        return root.data 
    return find_oldest_with_trait(root.left, trait)