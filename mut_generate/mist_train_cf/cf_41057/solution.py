"""
QUESTION:
Implement the `find_new_centroids` method that calculates the new centroids based on the given data and the current centroids. The `find_new_centroids` method takes two parameters: `centroids` and `data`. The `centroids` variable represents the current centroids of the clusters, where each centroid is a dictionary with 'cluster', 'x', and 'y' keys. The `data` variable represents the data points to be clustered, where each data point is a dictionary with 'cluster' and 'x' and 'y' keys.

The method should return a list of new centroids, where each new centroid is a dictionary with 'cluster', 'x', and 'y' keys. The new centroids should be calculated by averaging the positions of the data points belonging to each cluster. If a cluster has no data points, the current centroid should be retained as the new centroid.
"""

def find_new_centroids(centroids, data):
    new_centroids = []
    for centroid in centroids:
        cluster_points = [point for point in data if point['cluster'] == centroid['cluster']]
        if len(cluster_points) > 0:
            new_centroid = {
                'cluster': centroid['cluster'],
                'x': sum(point['x'] for point in cluster_points) / len(cluster_points),
                'y': sum(point['y'] for point in cluster_points) / len(cluster_points)
            }
            new_centroids.append(new_centroid)
        else:
            new_centroids.append(centroid)
    return new_centroids