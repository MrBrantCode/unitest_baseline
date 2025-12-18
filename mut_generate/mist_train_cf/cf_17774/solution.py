"""
QUESTION:
Create a function named `most_suitable_language` that takes two parameters: `languages` and `weights`. `languages` is a dictionary where the keys are the names of programming languages and the values are dictionaries with keys "performance", "scalability", "security", "ease_of_use", and "community_support", each representing a criterion for evaluating the language. `weights` is a dictionary where the keys are the same criteria and the values are the weights assigned to each criterion, representing their relative importance.

The function should return the name of the most suitable language based on the given criteria and weights, considering ties and additional factors in order of priority: available frameworks and libraries, compatibility with popular web servers, and developer job market demand.
"""

def most_suitable_language(languages, weights):
    def calculate_total_score(language, weights):
        total_score = 0
        for factor, weight in weights.items():
            total_score += language[factor] * weight
        return total_score

    ranked_languages = []
    for language, details in languages.items():
        total_score = calculate_total_score(details, weights)
        ranked_languages.append((language, total_score))
    ranked_languages.sort(key=lambda x: x[1], reverse=True)

    most_suitable_languages = [ranked_languages[0][0]]
    max_score = ranked_languages[0][1]
    for i in range(1, len(ranked_languages)):
        if ranked_languages[i][1] == max_score:
            most_suitable_languages.append(ranked_languages[i][0])
        else:
            break

    if len(most_suitable_languages) == 1:
        return most_suitable_languages[0]
    else:
        for language in most_suitable_languages:
            if language in languages:
                return language
        return most_suitable_languages[0]