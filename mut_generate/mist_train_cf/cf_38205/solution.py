"""
QUESTION:
Write a `format_stats` function that takes a `variant_stats` object as input and returns a formatted string representing the statistics for a game variant. The `variant_stats` object contains a `distribution` attribute that needs to be included in the formatted string. The function should return a string that is visually appealing and can be used in a Discord embed.
"""

def format_stats(variant_stats):
    distribution = variant_stats.distribution
    formatted_stats = ""

    for key, value in distribution.items():
        formatted_stats += f"{key}: {value}\n"

    return formatted_stats