"""
QUESTION:
Implement a function `get_unique_name(vdir, names)` that generates a unique name for a virtual directory `vdir` based on a list of existing names `names`. The function should extract the base name of the virtual directory from the last part of the `vdir` path and append a counter to it if the base name is already in `names`, until a unique name is generated. The unique name should be added to the `names` list and returned by the function.
"""

def get_unique_name(vdir, names):
    base_name = vdir.split('/')[-1]  
    unique_name = base_name
    counter = 1
    while unique_name in names:
        unique_name = f"{base_name}_{counter}"  
        counter += 1
    names.append(unique_name)  
    return unique_name