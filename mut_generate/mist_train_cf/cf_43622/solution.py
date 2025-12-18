"""
QUESTION:
Create a function `grammy_journey` that takes in an artist's name, the title of their album of the year, the number of nominations they have received, and a list of tuples containing the album's chart performance (the album title and the number of weeks it stayed on the charts). The function should return a dictionary with the following keys: 'artist', 'album_of_the_year', 'nominations', and 'chart_performance'. The 'chart_performance' value should be a list of dictionaries where each dictionary has 'album' and 'weeks_on_chart' keys. The function should not display any visual information, only organize the data.
"""

def grammy_journey(artist_name, album_of_the_year, nominations, chart_performance):
    """
    Organize an artist's Grammy journey data into a dictionary.

    Args:
        artist_name (str): The name of the artist.
        album_of_the_year (str): The title of the artist's album of the year.
        nominations (int): The number of nominations the artist has received.
        chart_performance (list of tuples): A list of tuples containing the album title and the number of weeks it stayed on the charts.

    Returns:
        dict: A dictionary containing the artist's Grammy journey data.
    """
    # Initialize the result dictionary
    result = {
        'artist': artist_name,
        'album_of_the_year': album_of_the_year,
        'nominations': nominations,
        'chart_performance': []
    }

    # Convert chart performance tuples to dictionaries and add to the result
    for album, weeks_on_chart in chart_performance:
        result['chart_performance'].append({
            'album': album,
            'weeks_on_chart': weeks_on_chart
        })

    return result