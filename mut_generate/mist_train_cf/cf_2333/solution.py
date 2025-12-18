"""
QUESTION:
Write a function named `calculate_average_age` that takes a list of tuples as input. The function should unpack the list of tuples, calculate the average age of people in the valid tuples, and return the average age rounded to the nearest whole number. 

Each tuple should have exactly 20 elements and meet the following criteria:
- The first element should be a string representing the person's name.
- The second element should be an integer representing the person's age.
- The third element should be a string representing the person's gender.
- The fourth element should be a string representing the person's occupation.
- The fifth element should be a float representing the person's salary.
- The sixth element should be a boolean indicating whether the person has a car or not.
- The seventh element should be a string representing the person's nationality.
- The eighth element should be a string representing the person's favorite color.
- The ninth element should be a string representing the person's favorite food.
- The tenth element should be a string representing the person's favorite animal.
- The eleventh to twentieth elements can be any valid data types.

If a tuple does not meet the above criteria, skip it and proceed with the next tuple. If the age of a person is not between 18 and 70, skip that person when calculating the average age.
"""

def calculate_average_age(tuples):
    total_age = 0
    count = 0

    for tuple in tuples:
        if len(tuple) != 20:
            continue
        if not (isinstance(tuple[0], str) and isinstance(tuple[1], int) and 
                isinstance(tuple[2], str) and isinstance(tuple[3], str) and 
                isinstance(tuple[4], float) and isinstance(tuple[5], bool) and 
                isinstance(tuple[6], str) and isinstance(tuple[7], str) and 
                isinstance(tuple[8], str) and isinstance(tuple[9], str)):
            continue
        if tuple[1] < 18 or tuple[1] > 70:
            continue
        
        total_age += tuple[1]
        count += 1

    return round(total_age / count) if count > 0 else 0