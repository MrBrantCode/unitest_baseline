"""
QUESTION:
Implement a function `average_mark_value` that calculates the average mark value for all characters based on the provided anchor data. The function takes a dictionary `anchor_data` as input, where each key is a character name and each value is another dictionary containing anchor information, including a 'mark' value. The function should return the average mark value as a float, calculated by summing up all mark values and dividing by the total number of characters. The function should work for any number of characters and their corresponding mark values.
"""

def average_mark_value(anchor_data: dict) -> float:
    total_marks = sum(anchor['mark'] for anchor in anchor_data.values())
    average_mark = total_marks / len(anchor_data)
    return average_mark