"""
QUESTION:
Create a function `calculate_student_grades` that takes a list of dictionaries as input, where each dictionary represents a student with a 'name' and a list of 'grades'. The function should return a list of dictionaries containing the student's name, their average grade rounded to the nearest integer, and a comment based on their grade. The comment should be assigned according to the following criteria: 
- "Excellent" if the average grade is 90 or above, 
- "Good" if the average grade is between 80 and 89, 
- "Average" if the average grade is between 70 and 79, 
- "Below Average" if the average grade is below 70.
"""

def calculate_student_grades(students):
    results = []
    
    for student in students:
        name = student['name']
        grades = student['grades']
        average_grade = round(sum(grades) / len(grades))
        
        if average_grade >= 90:
            comment = 'Excellent'
        elif average_grade >= 80:
            comment = 'Good'
        elif average_grade >= 70:
            comment = 'Average'
        else:
            comment = 'Below Average'
        
        results.append({'name': name, 'average_grade': average_grade, 'comment': comment})
    
    return results