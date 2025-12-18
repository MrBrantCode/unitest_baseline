"""
QUESTION:
Implement the `voxel3DThinning` function to perform 3D thinning on a given voxel set. The function should iteratively remove voxels from the input set until no further changes occur, preserving the essential structure of the original shape. The function should return the thinned voxel set.
"""

def voxel3DThinning(voxel_set):
    """
    Perform 3D thinning on the given voxel set.

    Args:
    voxel_set (set): A set of 3D voxels, where each voxel is represented as a tuple of three integers (x, y, z).

    Returns:
    set: The thinned voxel set.
    """

    # Define the 26 possible directions in a 3D grid
    directions = [(i, j, k) for i in range(-1, 2) for j in range(-1, 2) for k in range(-1, 2) if (i, j, k) != (0, 0, 0)]

    # Function to count the number of neighboring voxels
    def count_neighbors(x, y, z):
        count = 0
        for dx, dy, dz in directions:
            nx, ny, nz = x + dx, y + dy, z + dz
            if (nx, ny, nz) in voxel_set:
                count += 1
        return count

    # Function to check if a voxel is a border voxel
    def is_border_voxel(x, y, z):
        for dx, dy, dz in directions:
            nx, ny, nz = x + dx, y + dy, z + dz
            if (nx, ny, nz) not in voxel_set:
                return True
        return False

    # Main thinning loop
    changed = True
    while changed:
        changed = False
        voxels_to_remove = set()
        for x, y, z in voxel_set:
            # Check if voxel is a border voxel or has at least one neighboring voxel
            if is_border_voxel(x, y, z) or count_neighbors(x, y, z) < 2:
                voxels_to_remove.add((x, y, z))
                changed = True
        voxel_set -= voxels_to_remove

    return voxel_set