"""
QUESTION:
Write a function `convert_dates` that takes a list of dates in various formats and a desired output format. The function should convert each date to the desired output format, handling date inconsistencies and missing values. 

The function should be able to interpret dates in the following formats: "yyyy-mm-dd" and "mm.dd.yyyy". It should correctly convert dates in leap years and skip and mark missing values in the list as 'NaN'. If a date is not in a recognized format or does not exist, the function should return an error message.
"""

from datetime import datetime

def convert_dates(date_list, desired_format):
    original_formats = ["%Y-%m-%d", "%m.%d.%Y"]
    result = []
    for date in date_list:
        if date == "":
            result.append("NaN")
        else:
            for form in original_formats:
                try:
                    date_obj = datetime.strptime(date, form)
                    result.append(date_obj.strftime(desired_format))
                    break
                except ValueError:
                    pass
            else:
                result.append("Error: Date not in correct format or doesn't exist")
    return result