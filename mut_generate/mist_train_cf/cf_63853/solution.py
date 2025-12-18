"""
QUESTION:
Create a function named `get_stats` that takes a 3D matrix as input and returns a dictionary where each unique number in the matrix is a key, and the value is another dictionary with the count and average of that number. The function should ignore null values and handle duplicates by increasing the count and adding to the total each time the number is found.
"""

def get_stats(three_d_matrix):
    stats = {}  # This dictionary holds the statistics of the numbers

    # Traverse through the 3D matrix
    for matrix in three_d_matrix:
        for row in matrix:
            for ele in row:
                # Check if a non null value
                if ele is not None:
                    # If the element already exists in our stats dict
                    if ele in stats:
                        # Increase count by 1 and add the value to the total
                        stats[ele]['count'] += 1
                        stats[ele]['total'] += ele
                    else:
                        # If element hasn't be seen before, add it to our stats dict
                        stats[ele] = {'count': 1, 'total': ele}

    # Now calculate average for each distinct number
    for key in stats.keys():
        stats[key]['avg'] = stats[key]['total'] / stats[key]['count']

    return stats