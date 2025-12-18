"""
QUESTION:
Write a function called `process_data` that takes a list of tuples as input, where each tuple contains a name (string), an age (integer), and a city (string). The function should perform the following operations:
- Remove all duplicate tuples from the list based on the names.
- Sort the list in ascending order based on the ages.
- Calculate the sum of all the ages in the list.
- Find the average age of all the people in the list, rounded to 2 decimal places.
- Find the city with the highest number of people in the list.
 
The function should return the processed list, the sum of ages, the average age, and the city with the highest number of people.
"""

def process_data(data):
    # Remove all duplicate tuples based on names
    data = list(set(data))

    # Sort the list in ascending order based on ages
    data.sort(key=lambda tup: tup[1])

    # Calculate the sum of all ages in the list
    sum_of_ages = sum(age for _, age, _ in data)

    # Find the average age of all people in the list, rounded to 2 decimal places
    average_age = round(sum_of_ages / len(data), 2)

    # Find the city with the highest number of people in the list
    cities = {}
    for _, _, city in data:
        if city in cities:
            cities[city] += 1
        else:
            cities[city] = 1

    city_with_highest_count = max(cities, key=cities.get)

    return data, sum_of_ages, average_age, city_with_highest_count