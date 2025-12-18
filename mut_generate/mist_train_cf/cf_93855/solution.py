"""
QUESTION:
Write a function named "group_students" that takes a list of student objects as input, where each student object has "name" (string), "major" (string), and "age" (integer) attributes. The function should return a dictionary where the keys are the major names and the values are lists of student names belonging to that major, sorted in alphabetical order. The function should exclude majors without students and handle cases with additional student attributes.
"""

def group_students(student_list):
    result = {}
    
    for student in student_list:
        major = student["major"]
        name = student["name"]
        
        if major in result:
            result[major].append(name)
        else:
            result[major] = [name]
    
    for major in result:
        result[major].sort()
    
    return result