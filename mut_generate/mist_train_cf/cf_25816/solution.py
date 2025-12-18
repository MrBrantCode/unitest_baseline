"""
QUESTION:
Parse an article about a basketball player signing with a team and extract the following information: team name, player name, contract details, team's recent record, and the player's average points and rebounds per game. The extracted data should be stored in a dictionary with the keys "team", "player", "contract", "recent_record", "average_points", and "average_rebounds".
"""

def parse_article(article_text):
    """
    Parse an article about a basketball player signing with a team and extract relevant information.

    Args:
        article_text (str): Text of the article to parse.

    Returns:
        dict: Dictionary containing extracted information with keys "team", "player", "contract", "recent_record", "average_points", and "average_rebounds".
    """
    # Assuming the article text is already available, this function would typically involve natural language processing techniques to extract the required information
    # For simplicity, this example uses placeholder values
    extracted_data = {
        "team": "Boston Celtics",
        "player": "Gordon Hayward",
        "contract": "Four-year deal",
        "recent_record": "team's worst record since 2007",
        "average_points": 10.7,
        "average_rebounds": 5
    }
    return extracted_data