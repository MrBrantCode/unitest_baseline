"""
QUESTION:
Implement a function named `get_deepest_point` that takes an ocean's name as a parameter and returns the deepest point in that ocean and the corresponding depth. The function should have access to a dictionary containing the five deepest oceans and the deepest point in each of these oceans along with its approximate depth in meters. The function should include error handling for cases where the ocean's name is not found in the dictionary. Additionally, implement a search algorithm to find and display the ocean with the deepest point and its depth.
"""

# Create dictionary with information about the deepest oceans and points
oceans_depth = {
    'Pacific': {'Challenger Deep': 10916},
    'Atlantic': {'Milwaukee Deep': 8605},
    'Indian': {'Java Trench': 7255},
    'Southern': {'South Sandwich Trench': 7235},
    'Arctic': {'Litke Deep': 5450}
}

def get_deepest_point(ocean):
    """Return the deepest point in the ocean and corresponding depth"""
    try:
        point_depth = oceans_depth[ocean]
        point, depth = list(point_depth.items())[0]
        return point, depth
    except KeyError:
        return None, None