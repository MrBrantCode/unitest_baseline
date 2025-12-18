"""
QUESTION:
Calculate the average age of users in a given dataset using MapReduce, excluding users below the age of 18. The dataset is assumed to be comma-separated with user ID and age in the first and second columns respectively. Design a mapper function to filter and emit the age of users, a reducer function to calculate the sum and count of ages, and a main function to execute the MapReduce job and compute the average age.
"""

def calculate_average_age(dataset):
    total_age = 0
    total_count = 0
    
    for line in dataset:
        data = line.split(',')
        age = int(data[1])
        
        if age >= 18:
            total_age += age
            total_count += 1
    
    if total_count == 0:
        return 0
    else:
        return total_age / total_count