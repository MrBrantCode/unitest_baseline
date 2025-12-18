"""
QUESTION:
Create a function named `filter_and_sort_students` that takes a dictionary of students with their respective height, weight, and age, along with the minimum height, weight, and age as input parameters. The function should filter out students with height, weight, and age above the minimum values and return a list of the remaining students sorted in descending order by age. Note that the comparison should be strict (greater than), not inclusive (greater than or equal to).
"""

def filter_and_sort_students(students_dict, min_height, min_weight, min_age):
    # filter students above the minimal values
    filtered_students = {name: values for name, values in students_dict.items() 
                            if values[0] > min_height and values[1] > min_weight and values[2] > min_age}

    # sort students by age in descending order
    sorted_students = sorted(filtered_students.items(), key=lambda student: student[1][2], reverse=True)

    return sorted_students