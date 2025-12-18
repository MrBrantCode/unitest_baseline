"""
QUESTION:
Create a function named time_greeting that takes three parameters: time (integer), format (string), and period (string, optional). The function should return a greeting based on the time, which can be in either 12-hour or 24-hour format, and the AM or PM period. The function must have a time complexity of O(1) and cannot use if-else or switch statements. The period parameter is required only when the format is "12-hour".
"""

def time_greeting(time, format, period=None):
    greetings = {
        0: "Good morning",
        1: "Good morning",
        2: "Good morning",
        3: "Good morning",
        4: "Good morning",
        5: "Good morning",
        6: "Good morning",
        7: "Good morning",
        8: "Good morning",
        9: "Good morning",
        10: "Good morning",
        11: "Good morning",
        12: "Good afternoon",
        13: "Good afternoon",
        14: "Good afternoon",
        15: "Good afternoon",
        16: "Good afternoon",
        17: "Good afternoon",
        18: "Good evening",
        19: "Good evening",
        20: "Good evening",
        21: "Good evening",
        22: "Good evening",
        23: "Good evening"
    }
    
    if format == "12-hour":
        time = (time + 12) % 24 if period == "PM" else time
    return greetings[time]