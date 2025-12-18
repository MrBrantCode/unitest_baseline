"""
QUESTION:
Create a function called `cluster_dates_by_week` that takes a list of ISO 8601 compliant date strings as input and returns a dictionary where each key represents a week and its corresponding value is a list of dates that fall within that week. The dates should be clustered into 7-day spans, with the first date of the input list determining the start of the first week.
"""

from datetime import datetime, timedelta

def cluster_dates_by_week(dates):
    """
    Cluster a list of ISO 8601 compliant date strings into 7-day spans.

    Args:
        dates (list): A list of ISO 8601 compliant date strings.

    Returns:
        dict: A dictionary where each key represents a week and its corresponding value is a list of dates that fall within that week.
    """

    # Convert strings into date objects
    converted_dates = [datetime.strptime(d, '%Y-%m-%d') for d in dates]

    # Sort dates chronologically
    converted_dates.sort()

    clusters = {}
    week = 0
    start_date = None

    for date in converted_dates:
        if start_date is None or date - start_date >= timedelta(days=7):
            week += 1
            start_date = date
        if week not in clusters:
            clusters[week] = []
        clusters[week].append(date.strftime('%Y-%m-%d'))

    return clusters