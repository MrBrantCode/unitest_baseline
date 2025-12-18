"""
QUESTION:
Create a function `recommend_products(customer_id)` that generates personalized product recommendations based on a customer's past purchases. The function should take into account factors such as product categories and price ranges to provide targeted marketing strategies for each customer. 

The function should be able to handle a list of customer purchase history, where each purchase is represented as a dictionary containing the customer's ID, product ID, product category, price range, and purchase frequency. 

The function should return a list of the top 3 product recommendations for the given customer, where each recommendation is a dictionary containing the product category, price range, and probability of the customer moving to that combination.
"""

import numpy as np

def recommend_products(customer_id, customer_purchase_history, categories, price_ranges):
    # Create a transition matrix for product categories
    category_matrix = np.zeros((len(categories), len(categories)))
    for i, category_i in enumerate(categories):
        for j, category_j in enumerate(categories):
            transitions = [x for x in customer_purchase_history if x['category'] == category_i]
            transitions_to_j = [x for x in transitions if x['category'] == category_j]
            total_transitions = len(transitions)
            if total_transitions > 0:
                category_matrix[i, j] = len(transitions_to_j) / total_transitions

    # Create a transition matrix for price ranges
    price_matrix = np.zeros((len(price_ranges), len(price_ranges)))
    for i, price_i in enumerate(price_ranges):
        for j, price_j in enumerate(price_ranges):
            transitions = [x for x in customer_purchase_history if x['price_range'] == price_i]
            transitions_to_j = [x for x in transitions if x['price_range'] == price_j]
            total_transitions = len(transitions)
            if total_transitions > 0:
                price_matrix[i, j] = len(transitions_to_j) / total_transitions

    # Retrieve customer purchase history
    customer_history = [x for x in customer_purchase_history if x['customer_id'] == customer_id]
    if len(customer_history) == 0:
        return []
    
    # Compute the probability of moving to each category and price range
    category_probs = np.sum(category_matrix, axis=0)
    category_probs /= np.sum(category_probs)
    price_probs = np.sum(price_matrix, axis=0)
    price_probs /= np.sum(price_probs)
    
    # Compute the probability of moving from each category and price range to a new product
    category_transitions = [np.dot(category_matrix[i], price_probs) for i in range(len(categories))]
    price_transitions = [np.dot(price_matrix[i], category_probs) for i in range(len(price_ranges))]
    
    # Create a list of potential product recommendations
    recommendations = []
    for i, category_i in enumerate(categories):
        for j, price_j in enumerate(price_ranges):
            probability = customer_history[-1]['freq'] * category_transitions[i] * price_transitions[j]
            recommendations.append({'category': category_i, 'price_range': price_j, 'probability': probability})
    
    # Sort the list of recommendations by probability and return the top 3
    recommendations = sorted(recommendations, key=lambda x: x['probability'], reverse=True)
    return recommendations[:3]