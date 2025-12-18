"""
QUESTION:
Implement the `fitness_distance` function that takes two parameters: `genomes` (a list of strings) and `engine` (an optimization engine object). The function should calculate the distance-based fitness scores for each genome in the `genomes` list. The calculation involves retrieving scores from the `engine`, finding the maximum distance from `engine.track.distance_matrix`, and then dividing each score by the maximum distance. The function should return a list of distance-based fitness scores.
"""

def fitness_distance(genomes, engine):
    scores = engine.get_scores()
    max_distance = engine.track.distance_matrix.max()
    fitness_scores = [score / max_distance for score in scores]
    return fitness_scores