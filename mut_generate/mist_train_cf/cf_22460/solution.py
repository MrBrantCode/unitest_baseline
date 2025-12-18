"""
QUESTION:
Implement a function `calculate_rankings` that takes in five parameters: `ratings`, `dates`, `views`, `comments`, and `reputations`. The function should calculate a score for each submission based on the given parameters, with weights assigned as follows: 40% for `ratings`, 30% for `dates` (with more recent dates scoring higher), 20% for `views`, 10% for `comments`, and 5% for `reputations`. The function should return the rankings of the submissions in descending order of their calculated scores.
"""

import numpy as np

def calculate_rankings(ratings, dates, views, comments, reputations):
    weights = {
        'ratings': 0.4,
        'dates': 0.3,
        'views': 0.2,
        'comments': 0.1,
        'reputation': 0.05
    }
    
    scores = np.zeros(len(ratings))
    
    for i in range(len(ratings)):
        scores[i] += ratings[i] * weights['ratings']
        days_ago = (np.max(dates) - dates[i]).days
        scores[i] += (1 / (1 + days_ago)) * weights['dates']
        scores[i] += views[i] * weights['views']
        scores[i] += comments[i] * weights['comments']
        scores[i] += reputations[i] * weights['reputation']
        
    rankings = np.argsort(scores)[::-1]
    
    return rankings