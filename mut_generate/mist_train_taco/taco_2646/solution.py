"""
QUESTION:
The weather in Takahashi's town changes day by day, in the following cycle: Sunny, Cloudy, Rainy, Sunny, Cloudy, Rainy, ...
Given is a string S representing the weather in the town today. Predict the weather tomorrow.

-----Constraints-----
 - S is Sunny, Cloudy, or Rainy.

-----Input-----
Input is given from Standard Input in the following format:
S

-----Output-----
Print a string representing the expected weather tomorrow, in the same format in which input is given.

-----Sample Input-----
Sunny

-----Sample Output-----
Cloudy

In Takahashi's town, a sunny day is followed by a cloudy day.
"""

def predict_tomorrow_weather(today_weather: str) -> str:
    if today_weather == 'Sunny':
        return 'Cloudy'
    elif today_weather == 'Cloudy':
        return 'Rainy'
    elif today_weather == 'Rainy':
        return 'Sunny'
    else:
        raise ValueError("Invalid input. Today's weather must be 'Sunny', 'Cloudy', or 'Rainy'.")