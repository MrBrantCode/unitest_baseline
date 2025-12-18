"""
QUESTION:
Write a function named `count_working_days` that calculates the number of working days between two given dates, excluding weekends, holidays, and specific dates from an exclusion list. The function should handle edge cases such as invalid dates, input data not in the correct format, and exclusion list dates falling on weekends and holidays. The function should be able to efficiently process up to 1,000,000 records.

The function should take in the following parameters: `date1`, `date2`, `holidays`, and `exclusion_list`. The function should return the number of working days between `date1` and `date2` after applying the specified exclusions.
"""

import pandas as pd
import datetime

def count_working_days(date1, date2, holidays=[], exclusion_list=[]):
    try:
        d1 = pd.to_datetime(date1)
        d2 = pd.to_datetime(date2)

        # check date1 < date2
        if d2 < d1:
            print("date1 should be older than date2")
            return None

        # Generate all weekdays between d1 and d2
        all_days = pd.date_range(start=d1, end=d2, freq='B')

        # Exclude the holidays
        all_days = all_days[~all_days.isin(holidays)]

        # Exclude the dates in the exclusion list
        all_days = all_days[~all_days.isin(exclusion_list)]

        # Return number of days left
        return len(all_days)

    except ValueError:
        print("One of the inputs is not a valid date.")
        return None