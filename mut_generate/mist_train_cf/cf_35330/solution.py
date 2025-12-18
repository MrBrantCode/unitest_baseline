"""
QUESTION:
Implement the `greedy_algorithm_2` method to optimize the target function `tf_res` using a fine vector `U` and an order parameter. The method should sort the fine vector based on the target function's value in descending order and then iteratively select elements from the sorted vector based on the order parameter. The order parameter determines the selection order: 1 for ascending order, 2 for descending order, and other values for additional selection strategies. The method should return the optimized result based on the selected elements.
"""

def greedy_algorithm_2(U, tf_res, order):
    sorted_vector = sorted(U, key=tf_res, reverse=True)
    selected_elements = []

    for i in range(len(sorted_vector)):
        if order == 1:
            selected_elements.append(sorted_vector[i])
        elif order == 2:
            selected_elements.append(sorted_vector[len(sorted_vector) - 1 - i])
        else:
            # Handle other order parameter values (e.g., alternate selection strategies)
            pass

    optimized_result = tf_res(selected_elements)
    return optimized_result