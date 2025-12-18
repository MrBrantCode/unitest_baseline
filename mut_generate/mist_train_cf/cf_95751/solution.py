"""
QUESTION:
Implement a function `mahalanobis_distance(data_points, test_point)` that calculates the Mahalanobis distance between a point and a distribution. The function should take two parameters: `data_points`, a list of tuples representing the coordinates of the data points in the distribution, and `test_point`, a tuple representing the coordinates of the point to calculate the distance from. 

The function should return the Mahalanobis distance between the test point and the distribution. It should be able to handle cases where the number of variables (coordinates) in the data points and test point is not the same.

Note: The function should not use any built-in functions or libraries for matrix calculations.
"""

def mahalanobis_distance(data_points, test_point):
    # Step 1: Calculate the covariance matrix
    num_dimensions = len(data_points[0])  # Number of variables (coordinates)
    
    # Calculate the mean of each variable
    means = []
    for i in range(num_dimensions):
        total = sum(data[i] for data in data_points)
        mean = total / len(data_points)
        means.append(mean)
    
    # Calculate the covariance matrix
    covariance_matrix = [[0] * num_dimensions for _ in range(num_dimensions)]
    for data in data_points:
        difference = [data[i] - means[i] for i in range(num_dimensions)]
        for i in range(num_dimensions):
            for j in range(num_dimensions):
                covariance_matrix[i][j] += (difference[i] * difference[j]) / (len(data_points) - 1)
    
    # Step 2: Calculate the inverse of the covariance matrix
    # Add a small constant to the diagonal elements for numerical stability
    epsilon = 0.0001
    for i in range(num_dimensions):
        covariance_matrix[i][i] += epsilon
    
    # Calculate the inverse of the covariance matrix using the matrix inverse formula
    inverse_covariance_matrix = [[0] * num_dimensions for _ in range(num_dimensions)]
    for i in range(num_dimensions):
        for j in range(num_dimensions):
            if i == j:
                inverse_covariance_matrix[i][j] = 1 / covariance_matrix[i][j]
            else:
                inverse_covariance_matrix[i][j] = -covariance_matrix[i][j] / (covariance_matrix[i][i] * covariance_matrix[j][j])
    
    # Step 3: Calculate the difference vector between the test point and the mean of the distribution
    difference_vector = [test_point[i] - means[i] for i in range(num_dimensions)]
    
    # Step 4: Calculate the transpose of the difference vector
    transpose_vector = [[difference_vector[i]] for i in range(num_dimensions)]
    
    # Step 5: Multiply the difference vector with the inverse of the covariance matrix
    product_vector = [[0] for _ in range(num_dimensions)]
    for i in range(num_dimensions):
        for j in range(num_dimensions):
            product_vector[i][0] += inverse_covariance_matrix[i][j] * transpose_vector[j][0]
    
    # Step 6: Calculate the dot product of the result from step 5 with the difference vector
    dot_product = 0
    for i in range(num_dimensions):
        dot_product += product_vector[i][0] * difference_vector[i]
    
    # Step 7: Take the square root of the result from step 6 to get the Mahalanobis distance
    mahalanobis_distance = dot_product ** 0.5
    
    # Step 8: Return the Mahalanobis distance
    return mahalanobis_distance