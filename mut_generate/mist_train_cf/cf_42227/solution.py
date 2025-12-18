"""
QUESTION:
Implement a function `find_nearest_cluster_centers` that calculates the distance between a set of input data points and the stored cluster centers and returns the index of the nearest cluster center for each input data point. 

The function takes the following parameters: 
- `cluster_file`: The file path to the memory-mapped file where the cluster centers are stored.
- `n_cluster`: The number of clusters.
- `info`: A dictionary containing information about the data, including `dstore_fp16` and `hidden_size`.
- `cluster_mmap`: The memory-mapped array containing the cluster centers.
- `train_in_memory`: An array containing the input data points for which you need to find the nearest cluster center.
- `index`: An index structure used to efficiently search for the nearest cluster center.

The function should return a list of indices, where each index represents the nearest cluster center for the corresponding input data point.
"""

def find_nearest_cluster_centers(cluster_file, n_cluster, info, cluster_mmap, train_in_memory, index):
    # Load the memory-mapped array containing the cluster centers
    cluster_mmap = np.memmap(cluster_file, 
                             dtype=np.float16 if info['dstore_fp16'] else np.float32,
                             mode="r",
                             shape=(n_cluster, info['hidden_size']))

    # Search for the nearest cluster center for each input data point
    _, labels = index.search(train_in_memory, 1)

    return labels.flatten().tolist()