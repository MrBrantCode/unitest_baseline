"""
QUESTION:
Create a function `recreate_transform(es, name)` that takes in two parameters: 
- `es`: A list of strings representing elementary transformations, either "rotate" or "mirror".
- `name`: A string representing the name of the transformation to be recreated.

The function should return a string representing the transformation that results from applying the elementary transformations in the list `es` in the order they appear, and then applying the transformation indicated by the `name` parameter. If the `name` parameter is not valid, the function should return "Invalid transformation name".
"""

def transform(es, name):
    transformation = ""
    for e in es:
        if e == "rotate":
            transformation = "rotated " + transformation
        elif e == "mirror":
            transformation = "mirrored " + transformation
    
    if name == "rotate":
        transformation = "rotated " + transformation
    elif name == "mirror":
        transformation = "mirrored " + transformation
    else:
        return "Invalid transformation name"
    
    return transformation