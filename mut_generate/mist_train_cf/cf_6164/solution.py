"""
QUESTION:
Function name: process_data

You are given a list of tuples, where each tuple contains a name (string), an age (integer), and a city (string). Write a program that performs the following operations on the list:
1. Remove all duplicate tuples from the list based on the names.
2. Sort the list in ascending order based on the ages.
3. Calculate the sum of all the ages in the list.
4. Find the average age of all the people in the list, rounded to 2 decimal places.
5. Find the city with the highest number of people in the list.
6. Print the final list, the sum of ages, the average age, and the city with the highest number of people.
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
    highest_count = cities[city_with_highest_count]

    return data, sum_of_ages, average_age, city_with_highest_count, highest_count