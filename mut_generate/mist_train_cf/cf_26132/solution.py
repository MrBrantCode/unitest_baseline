"""
QUESTION:
Create a function to display the current weather data. The function should take a dictionary containing 'temperature', 'humidity', 'windSpeed', and 'pressure' as input and return an HTML string to display the current weather with the given data. The HTML string should have the temperature, humidity, wind speed, and barometric pressure in separate paragraphs.
"""

def weather_data_display(weather_data):
    """
    This function takes a dictionary containing 'temperature', 'humidity', 'windSpeed', and 'pressure'
    as input and returns an HTML string to display the current weather with the given data.

    Args:
        weather_data (dict): A dictionary containing weather data.

    Returns:
        str: An HTML string to display the current weather.
    """
    return f"""
    <html>
      <head>
        <title>Current Weather</title>
      </head>
      <body>
        <p>Temperature: {weather_data['temperature']}</p>
        <p>Humidity: {weather_data['humidity']}%</p>
        <p>Wind Speed: {weather_data['windSpeed']} m/s</p>
        <p>Barometric Pressure: {weather_data['pressure']} hPa</p>
      </body>
    </html>
    """