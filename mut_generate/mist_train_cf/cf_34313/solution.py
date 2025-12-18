"""
QUESTION:
Implement the `map_global_to_local` function, which takes in 6 parameters: `lx` and `ly` representing the lattice grid size in the x and y directions, `x_size` and `y_size` representing the number of processes in the x and y directions, and `global_x` and `global_y` representing the global coordinates. The function should return a tuple containing the process coordinates and the local x and y coordinates for the given global coordinates. The process coordinates should be in the range [0, x_size) and [0, y_size), and the local coordinates should be in the range [0, lx // x_size) and [0, ly // y_size).
"""

def map_global_to_local(lx, ly, x_size, y_size, global_x, global_y):
    """
    Maps global coordinates to local coordinates in a parallel computing environment.

    Args:
        lx (int): lattice grid size in x direction
        ly (int): lattice grid size in y direction
        x_size (int): number of processes in x direction
        y_size (int): number of processes in y direction
        global_x (int): global x coordinate
        global_y (int): global y coordinate

    Returns:
        tuple: process coordinates, local x coordinate, and local y coordinate
    """
    # Calculate the size of each subgrid in x and y directions
    subgrid_x_size = lx // x_size
    subgrid_y_size = ly // y_size

    # Calculate the process coordinates
    process_x = global_x // subgrid_x_size
    process_y = global_y // subgrid_y_size

    # Calculate the local coordinates within the process
    local_x = global_x % subgrid_x_size
    local_y = global_y % subgrid_y_size

    return (process_x, process_y, local_x, local_y)