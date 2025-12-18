"""
QUESTION:
Create a function `cluster_objects` that takes a list of objects as input. Each object has three attributes: `shape`, `color`, and `size`. The function should group the objects into four clusters based on their attributes. The function should be able to handle both categorical (`shape` and `color`) and numerical (`size`) data.

Restrictions: The function should not use any machine learning libraries or algorithms. It should use simple conditional logic to group the objects. The function should return the cluster assignments for each object.
"""

class Object:
    def __init__(self, id, shape, color, size):
        self.id = id
        self.shape = shape
        self.color = color
        self.size = size

def cluster_objects(objects):
    """
    This function groups objects into four clusters based on their attributes.
    
    Parameters:
    objects (list): A list of Object instances.
    
    Returns:
    cluster_assignments (dict): A dictionary with object id as key and cluster assignment as value.
    """
    cluster_assignments = {}
    
    for object in objects:
        if object.shape in ['oval', 'octagonal']:
            if object.size < 10:
                cluster_assignments[object.id] = 'Group A'
            else:
                cluster_assignments[object.id] = 'Group B'
        else:
            if object.color in ['yellow', 'orange']:
                cluster_assignments[object.id] = 'Group C'
            else:
                cluster_assignments[object.id] = 'Group D'
    
    return cluster_assignments