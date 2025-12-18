"""
QUESTION:
Implement a k-nearest neighbors model from scratch to classify iris species. The model should not use any pre-existing k-NN libraries or functions, and should include functionality for calculating different types of distance metrics such as Euclidean, Manhattan, and Minkowski. Enhance the model by using a weighted voting system based on distance for the predictions.

Your model should take the following parameters as input:

- X_train: Training features
- X_test: Testing features
- y_train: Training labels
- k: Number of neighbors
- distance_metric: Type of distance metric to use (Euclidean, Manhattan, Minkowski)

The function should return the predicted labels for the test data.

Use the iris dataset from scikit-learn, normalize the data, and divide it into training and testing datasets maintaining stratified sampling. 

Perform a grid search to tune the hyperparameters (k and distance metric) using 10-fold cross-validation. Evaluate the model's performance using a confusion matrix, precision, recall, and f1-score. 

Restrictions:

- Do not use any pre-existing k-NN libraries or functions.
- Do not use any pre-existing grid search CV libraries.
- Implement the grid search manually.
- Perform 10-fold cross-validation for each combination of hyperparameters.
"""

def knn(X_train, X_test, y_train, k, distance_metric, p=3):
    """
    K-Nearest Neighbors model function.

    Parameters:
    X_train (array): Training features.
    X_test (array): Testing features.
    y_train (array): Training labels.
    k (int): Number of neighbors.
    distance_metric (str): Type of distance metric to use (Euclidean, Manhattan, Minkowski).
    p (int): Minkowski distance parameter. Default is 3.

    Returns:
    array: Predicted labels for the test data.
    """

    # Function for Calculating Different Types of Distance Metrics
    def euclidean_distance(x, y): return ((x - y) ** 2).sum() ** 0.5

    def manhattan_distance(x, y): return (abs(x - y)).sum()

    def minkowski_distance(x, y, p): return ((abs(x - y)) ** p).sum() ** (1/p)

    predictions = []
    for test_instance in X_test:
        distances = []
        for index, train_instance in enumerate(X_train):
            if distance_metric == 'euclidean':
                dist = euclidean_distance(test_instance, train_instance)
            elif distance_metric == 'manhattan':
                dist = manhattan_distance(test_instance, train_instance)
            elif distance_metric == 'minkowski':
                dist = minkowski_distance(test_instance, train_instance, p)
            distances.append((index, dist))
        distances.sort(key=lambda x: x[1])
        neighbors = [distances[i] for i in range(k)]
        class_votes = [y_train[neighbor[0]] for neighbor in neighbors]
        winner = Counter(class_votes).most_common(1)[0][0]
        predictions.append(winner)
    return np.array(predictions)