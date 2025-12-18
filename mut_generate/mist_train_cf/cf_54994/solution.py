"""
QUESTION:
Write a function `analyze_age` that takes a nested list of people's information as input, where the first sublist contains the header ["Name", "Age"] and the subsequent sublists contain the name and age of each person. The function should return the average age, median age, the name of the youngest person, and the name of the oldest person. The function should handle potential exceptions for missing data or non-numeric age entries.
"""

def analyze_age(data):
    try:
        ages = [int(person[1]) for person in data[1:]]
    except ValueError:
        return "Some age entries are not valid"
        
    average_age = sum(ages) / len(ages)
    
    sorted_ages = sorted(ages)
    if len(sorted_ages) % 2 == 0:
        median_age = (sorted_ages[len(sorted_ages) // 2] + sorted_ages[len(sorted_ages) // 2 - 1]) / 2
    else:
        median_age = sorted_ages[len(sorted_ages) // 2]
        
    young_index = ages.index(min(ages))
    old_index = ages.index(max(ages))
    
    youngest_person = data[young_index + 1][0]
    oldest_person = data[old_index + 1][0]
    
    return average_age, median_age, youngest_person, oldest_person