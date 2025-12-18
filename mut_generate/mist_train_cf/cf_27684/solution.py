"""
QUESTION:
Implement the `team_standings` function, which takes a league name and a year as input, to retrieve and process the relevant data from the `info_all` list of dictionaries, each containing team statistics for a specific league and year. The function should return a list of dictionaries representing the team standings for the specified league and year, sorted by team position. If no standings are found, return a message indicating their unavailability.
"""

def team_standings(league, year):
    """Returns team standings"""
    standings = [stats_temp for stats_temp in info_all if 'league' in stats_temp and 'year' in stats_temp and stats_temp['league'] == league and stats_temp['year'] == year]
    if not standings:
        return f"No standings available for {league} in {year}"
    
    standings.sort(key=lambda x: x['position'])  # Sort standings based on position
    return standings