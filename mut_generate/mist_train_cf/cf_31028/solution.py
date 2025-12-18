"""
QUESTION:
Calculate the vertex normal vectors for a given mesh by averaging the normal vectors of the triangles that share each vertex. 

The function `calculate_vertex_normals` should take three parameters: 
- `tri_elements`: A 2D numpy array representing the triangular elements of the mesh, where each row contains the vertex indices of a single triangle.
- `tri_normal_vec`: A 2D numpy array representing the normal vectors of the triangles, where each row contains the normal vector of a single triangle.
- `surf_vindex`: A 1D numpy array containing the indices of the vertices on the mesh surface.

The function should return a 2D numpy array `vtx_normal_vec` representing the normal vectors at each vertex on the mesh surface. The normal vector for each vertex should be calculated by averaging the normal vectors of the triangles that share that vertex.
"""

import numpy as np

def calculate_vertex_normals(tri_elements, tri_normal_vec, surf_vindex):
    vtx_normal_vec = np.zeros((surf_vindex.size, 3))
    for i, iv in enumerate(surf_vindex):
        iv_tri_index = np.argwhere(tri_elements == iv)[:, 0]
        iv_tri_nv = tri_normal_vec[iv_tri_index]
        vtx_normal_vec[i] = iv_tri_nv.mean(axis=0)  # Changed from sum to mean
    return vtx_normal_vec