"""
QUESTION:
Construct a function `get_number_of_days` that takes two parameters: `month` and `calendar_system` (with a default value of `'Gregorian'`). The function should return the number of days in the specified month according to the given calendar system. It should handle different calendar systems such as Gregorian, Julian, and Islamic, and return an error message if an invalid month name or calendar system is provided.
"""

def get_number_of_days(month, calendar_system='Gregorian'):
    days_in_month = {
        'Gregorian': {
            'January': 31,
            'February': 28,
            'March': 31,
            'April': 30,
            'May': 31,
            'June': 30,
            'July': 31,
            'August': 31,
            'September': 30,
            'October': 31,
            'November': 30,
            'December': 31
        },
        'Julian': {
            'January': 31,
            'February': 29,
            'March': 31,
            'April': 30,
            'May': 31,
            'June': 30,
            'July': 31,
            'August': 31,
            'September': 30,
            'October': 31,
            'November': 30,
            'December': 31
        },
        'Islamic': {
            'Muharram': 30,
            'Safar': 29,
            'Rabi al-Awwal': 30,
            'Rabi al-Thani': 29,
            'Jumada al-Awwal': 30,
            'Jumada al-Thani': 29,
            'Rajab': 30,
            'Shaban': 29,
            'Ramadan': 30,
            'Shawwal': 29,
            'Dhu al-Qadah': 30,
            'Dhu al-Hijjah': 29
        }
    }

    if calendar_system not in days_in_month:
        return 'Invalid calendar system.'

    if month not in days_in_month[calendar_system]:
        return 'Invalid month name.'

    return days_in_month[calendar_system][month]