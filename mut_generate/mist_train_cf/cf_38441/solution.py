"""
QUESTION:
Write a Python function `determine_date_specificity(user_input)` that takes a string representing a date as input and returns the specificity of the date. The function should determine the specificity based on predefined date patterns, which include full dates, dates with only month and year, and dates with only the year. The function should return one of the following specificities: 'full' for a complete date, 'month_year' for a date with only month and year, or 'year' for a date with only the year. The function should use a helper function `date_from_pattern(user_input, pattern)` to extract the date based on a specific pattern, and it should iterate through the predefined patterns to determine the specificity.
"""

def determine_date_specificity(user_input):
    full_date_patterns = ['%B %d, %Y', '%m/%d/%Y', '%m-%d-%Y']
    month_year_date_patterns = ['%B %Y', '%m/%Y', '%m-%Y']
    year_date_patterns = ['%Y']

    def date_from_pattern(user_input, pattern):
        from datetime import datetime
        try:
            return datetime.strptime(user_input, pattern)
        except ValueError:
            return None

    for pattern in full_date_patterns:
        maybe_date = date_from_pattern(user_input, pattern)
        if maybe_date is not None:
            return 'full'

    for pattern in month_year_date_patterns:
        maybe_date = date_from_pattern(user_input, pattern)
        if maybe_date is not None:
            return 'month_year'

    for pattern in year_date_patterns:
        maybe_date = date_from_pattern(user_input, pattern)
        if maybe_date is not None:
            return 'year'