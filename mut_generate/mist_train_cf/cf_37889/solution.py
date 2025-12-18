"""
QUESTION:
Implement a function `validate_cron(cron_expression: str) -> bool` that takes a cron expression as input and returns `True` if the expression is valid, and `False` otherwise. A valid cron expression must consist of exactly five space-separated fields representing minute, hour, day of the month, month, and day of the week. Each field must contain a valid value or a valid range of values, as specified below:
- Minute: 0-59
- Hour: 0-23
- Day of the month: 1-31
- Month: 1-12 or names of the months (e.g., Jan, Feb, etc.)
- Day of the week: 0-7 or names of the days (0 and 7 represent Sunday)
"""

import re

def validate_cron(cron_expression: str) -> bool:
    fields = cron_expression.split()
    
    if len(fields) != 5:
        return False
    
    field_ranges = [
        (0, 59),  # Minute
        (0, 23),  # Hour
        (1, 31),  # Day of the month
        (1, 12),  # Month
        (0, 7)    # Day of the week
    ]
    
    for i, field in enumerate(fields):
        if i == 4 and field.lower() in ['sun', 'mon', 'tue', 'wed', 'thu', 'fri', 'sat']:
            continue  # Day of the week can also be represented by names
        if not re.match(r'^(\*|\d+|\d+-\d+)(\/\d+)?(,\d+(-\d+)?)*$', field):
            return False
        
        if '-' in field:
            start, end = map(int, field.split('-'))
            if not (field_ranges[i][0] <= start <= end <= field_ranges[i][1]):
                return False
        elif '/' in field:
            step = int(field.split('/')[1])
            if step < 1:
                return False
        elif field != '*':
            value = int(field)
            if not (field_ranges[i][0] <= value <= field_ranges[i][1]):
                return False
    
    return True