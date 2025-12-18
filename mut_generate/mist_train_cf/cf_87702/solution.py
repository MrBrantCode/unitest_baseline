"""
QUESTION:
Write a function `get_most_suitable_language` that determines the most suitable programming language for creating a high-performance web application based on a set of criteria. 

The function should take two parameters: `languages` and `weights`. The `languages` parameter should be a dictionary where the keys are the names of the languages and the values are dictionaries containing the criteria ratings for each language. The `weights` parameter should be a dictionary where the keys are the criteria names and the values are positive integer weights.

The function should rank the programming languages based on the given criteria and return the most suitable language. If there is a tie, the function should consider additional factors in order of priority: available frameworks and libraries, compatibility with popular web servers, and developer job market demand. 

The function should return a string indicating the most suitable language.
"""

def get_most_suitable_language(languages, weights):
    def calculate_total_score(language):
        return sum(rating * weights.get(criteria, 0) for criteria, rating in language.items())

    max_score = 0
    most_suitable_language = ""
    for language, ratings in languages.items():
        total_score = calculate_total_score(ratings)
        if total_score > max_score:
            max_score = total_score
            most_suitable_language = language
    return most_suitable_language