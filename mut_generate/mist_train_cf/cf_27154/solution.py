"""
QUESTION:
Write a function `calculate_direct_interactions(n_obs_tris, n_src_tris)` that takes two integers `n_obs_tris` and `n_src_tris` as input, representing the number of triangles in the observed scene and the source scene, respectively, and returns the total number of direct interactions between triangles in the observed scene and the source scene.
"""

def calculate_direct_interactions(n_obs_tris, n_src_tris):
    return n_obs_tris * n_src_tris