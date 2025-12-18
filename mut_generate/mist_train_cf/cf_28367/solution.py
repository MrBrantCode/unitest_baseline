"""
QUESTION:
Create a function `daily_temperature_averages_table` that takes a pandas DataFrame `sfo_q2_weather_sample` as input and returns a new DataFrame. The input DataFrame contains columns "valid" (timestamp) and "tmpf" (temperature in Fahrenheit), and other irrelevant columns. The output DataFrame should have two columns: "valid_date" (date extracted from the "valid" timestamp column) and "avg_tmpf" (average temperature in Fahrenheit for each day). The function should compute the average temperature for each day and return the result in the specified format.
"""

import pandas as pd

def daily_temperature_averages_table(sfo_q2_weather_sample: pd.DataFrame) -> pd.DataFrame:
    sfo_q2_weather_sample["valid_date"] = pd.to_datetime(sfo_q2_weather_sample["valid"]).dt.date
    return sfo_q2_weather_sample.groupby("valid_date")["tmpf"].mean().reset_index().rename(columns={"tmpf": "avg_tmpf"})