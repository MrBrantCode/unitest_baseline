"""
QUESTION:
Create a function `process_model_options` that takes three parameters: `return_distance_clusters` (a boolean, default False), `return_str` (a boolean, default False), and `model_type` (a string, with valid options "KMeans" and "NearestCentroids"). The function returns another function. If `return_distance_clusters` is True and `model_type` is "KMeans" or "NearestCentroids", the returned function should return the model clusters distances. If `return_str` is True, the returned function should return a string representation of the function. If both `return_distance_clusters` and `return_str` are False, the returned function should return None.
"""

from typing import Optional, Union

def process_model_options(return_distance_clusters: Optional[bool] = False, 
                          return_str: Optional[bool] = False, 
                          model_type: str = "KMeans") -> Union[str, None]:
    def model_clusters_distances():
        # Logic to calculate model clusters distances
        return "Model clusters distances"

    def function_str_representation():
        # Logic to generate string representation of the function
        return str(process_model_options)

    if return_distance_clusters and model_type in ["KMeans", "NearestCentroids"]:
        return model_clusters_distances
    elif return_str:
        return function_str_representation
    else:
        return None