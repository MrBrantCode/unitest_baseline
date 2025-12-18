"""
QUESTION:
Write a function `format_date(date)` that takes a string representing a date in the format 'Month Day, Year' (e.g., 'January 5th, 2021') and returns the date in the ISO 8601 format 'YYYY-MM-DD'. The function should handle month names, day ordinals (e.g., '1st', '2nd', etc.), and four-digit years. The returned date should have two-digit month and day representations (padding with a leading zero if necessary).
"""

def format_date(date):
    month_dict = {
        'January': '01', 'February': '02', 'March': '03', 'April': '04',
        'May': '05', 'June': '06', 'July': '07', 'August': '08',
        'September': '09', 'October': '10', 'November': '11', 'December': '12'
    }
    
    parts = date.split()
    month = parts[0]
    day = parts[1].rstrip('st,nd,rd,th').zfill(2)
    year = parts[2]
    
    formatted_date = f'{year}-{month_dict[month]}-{day}'
    
    return formatted_date