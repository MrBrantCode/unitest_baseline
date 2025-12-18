"""
QUESTION:
Write a function `generate_summary(article)` that takes a dictionary representing a news article as input and returns a concise summary of the article in less than 20 words. The input dictionary contains the article's title, job displacement information, and societal impact information. The function should extract relevant information from the article and generate a brief summary.
"""

def entrance(article):
    return f"{article['title']} - {article['displacement_info']} impact on jobs, {article['impact_info']} societal impact."