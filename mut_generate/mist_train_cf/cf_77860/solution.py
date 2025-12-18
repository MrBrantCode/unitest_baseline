"""
QUESTION:
Create a function `average_age_of_females` that takes JSON data as input, identifies individuals with "female" gender, accumulates their ages, and returns the average age of these female individuals. If there are no females in the data, the function should return `None`.
"""

def average_age_of_females(json_data):
    data = json.loads(json_data)
    sum_age = 0
    female_count = 0
    for i in range(len(data)):
        if data[i]['gender'] == 'female':
            sum_age += data[i]['age']
            female_count += 1
    if female_count > 0:
        return sum_age / female_count
    else:
        return None