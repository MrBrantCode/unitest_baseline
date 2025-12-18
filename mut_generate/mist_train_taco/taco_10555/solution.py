"""
QUESTION:
Implement a class/function, which should parse time expressed as `HH:MM:SS`, or `null/nil/None` otherwise.

Any extra characters, or minutes/seconds higher than 59 make the input invalid, and so should return `null/nil/None`.
"""

def parse_time_to_seconds(time_str: str) -> int:
    try:
        # Extract hours, minutes, and seconds from the input string
        h = int(time_str[:2])
        m = int(time_str[3:5])
        s = int(time_str[6:8])
        
        # Check if the input string has the correct length and format
        if len(time_str) != 8 or time_str[2] != ':' or time_str[5] != ':':
            return None
        
        # Check if minutes and seconds are within valid ranges
        if m >= 60 or s >= 60:
            return None
        
        # Calculate the total number of seconds
        total_seconds = s + m * 60 + h * 3600
        return total_seconds
    
    except (ValueError, IndexError):
        # Return None if there is any error in parsing the input
        return None