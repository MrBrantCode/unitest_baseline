"""
QUESTION:
Create a function named `rank_languages` that takes a dictionary of programming languages as input, where each language is associated with a dictionary of criteria (performance, scalability, security, ease of use, and community support) and their corresponding scores. The function should rank the languages based on these criteria, prioritizing performance in case of a tie, and return the name of the most suitable language. The input dictionary has the following structure: `{"language": {"performance": score, "scalability": score, "security": score, "ease_of_use": score, "community_support": score}}`.
"""

def rank_languages(languages):
    ranked_languages = sorted(languages.items(), key=lambda x: (x[1]['performance'], x[1]['scalability'], x[1]['security'], x[1]['ease_of_use'], x[1]['community_support']), reverse=True)
    return ranked_languages[0][0]