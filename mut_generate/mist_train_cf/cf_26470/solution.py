"""
QUESTION:
Write a function `populate_neighbor_lists(npoints, faces)` that takes in the number of points `npoints` and a list of faces `faces`, and returns a list of neighbor lists for each point in the mesh. The neighbor list for a point contains the indices of the points that are directly connected to it by an edge in the mesh, with no duplicates.

The function should follow these constraints:
- `npoints` is an integer representing the total number of points in the mesh (1 <= npoints <= 1000).
- `faces` is a list of lists, where each inner list represents a face in the mesh. Each face contains three distinct integers representing the indices of the vertices (0 <= vertex index < npoints).
- The output should be a list of lists, where the ith list represents the neighbor list for the ith point in the mesh.
"""

def populate_neighbor_lists(npoints, faces):
    neighbor_lists = [[] for _ in range(npoints)]

    for face in faces:
        v0, v1, v2 = face
        if v1 not in neighbor_lists[v0]:
            neighbor_lists[v0].append(v1)
        if v2 not in neighbor_lists[v0]:
            neighbor_lists[v0].append(v2)

        if v0 not in neighbor_lists[v1]:
            neighbor_lists[v1].append(v0)
        if v2 not in neighbor_lists[v1]:
            neighbor_lists[v1].append(v2)

        if v0 not in neighbor_lists[v2]:
            neighbor_lists[v2].append(v0)
        if v1 not in neighbor_lists[v2]:
            neighbor_lists[v2].append(v1)

    return neighbor_lists