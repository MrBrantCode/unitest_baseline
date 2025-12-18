"""
QUESTION:
Write a function named "group_students" that takes in a list of student objects, where each object contains "name" (string), "major" (string), and "age" (integer) attributes. The function should return a dictionary where the keys are the major names and the values are lists of student names belonging to that major, sorted in alphabetical order. Major names are case-sensitive, and only majors with students should be included in the dictionary. The function should handle cases with additional attributes in the student objects.
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