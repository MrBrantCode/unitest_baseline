"""
QUESTION:
Implement a method `generate_b_reference_codes` that takes a league, season, and date as input and generates b-reference codes for regular season and post-season games. The method should construct the b-reference codes for each month from October to June. The base URL for the league is obtained from the `LEAGUES_TO_PATH` dictionary, and the season is extracted from the input.

Restrictions:

- The `LEAGUES_TO_PATH` dictionary maps leagues to their corresponding base URLs.
- The input season should be in the format "YYYY-YYYY".
- The output should be stored in the `self.reg_s_codes_` and `self.post_s_codes_` lists for regular season and post-season games, respectively.
"""

def generate_b_reference_codes(league, season, date):
    """
    Generates b-reference codes for regular season and post-season games.

    Args:
    league (str): The league for which to generate b-reference codes.
    season (str): The season in the format "YYYY-YYYY".
    date (str): The date for which to generate b-reference codes.

    Returns:
    tuple: A tuple containing two lists. The first list contains b-reference codes for regular season games, 
           and the second list contains b-reference codes for post-season games.
    """
    LEAGUES_TO_PATH = {
        'nba': 'https://www.example.com/{0}/games/'
    }
    
    base_url = LEAGUES_TO_PATH[league].format(season.split('-')[1])
    months = ['october', 'november', 'december', 'january', 'february', 'march', 'april', 'may', 'june']
    reg_s_codes = []
    post_s_codes = []

    for month in months:
        reg_s_code = f"{base_url}{month}/{date}/regular"
        post_s_code = f"{base_url}{month}/{date}/postseason"
        reg_s_codes.append(reg_s_code)
        post_s_codes.append(post_s_code)
        
    return reg_s_codes, post_s_codes