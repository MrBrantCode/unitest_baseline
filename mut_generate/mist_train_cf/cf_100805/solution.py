"""
QUESTION:
Write a function named `calculate_average_attendance` that takes two parameters: `teams` (a list of team names) and `attendance` (a list of attendance numbers corresponding to each team). The function should assume that each team plays a certain number of home games per season (the number of games is not specified and should be a parameter). The function should return a dictionary where the keys are the team names and the values are the average attendance per game for each team.
"""

def calculate_average_attendance(teams, attendance, games_per_season):
    """
    Calculate the average attendance per game for each team.

    Args:
    teams (list): A list of team names.
    attendance (list): A list of attendance numbers corresponding to each team.
    games_per_season (int): The number of home games per season.

    Returns:
    dict: A dictionary where the keys are the team names and the values are the average attendance per game for each team.
    """
    average_attendance_dict = {}
    for team, att in zip(teams, attendance):
        average_attendance_dict[team] = att / games_per_season
    return average_attendance_dict